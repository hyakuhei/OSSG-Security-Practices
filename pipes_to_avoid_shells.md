
Python pipes to avoid shells
============================

You should take a look at the [shell injection document](/shell_injection.md) before this one.


A lot of the time, our codebase uses `shell=True` because it's
convenient. The shell provides the ability to pipe things around
without buffering them in memory, and makes it easy to chain commands.

Here's a simple function that uses curl to grab a website, and pipe it
directly to the `wordcount` program to tell us how many lines there
are in the source code.

### Incorrect

```python
def count_lines(website):
    return subprocess.check_output('curl %s | wc -l' % website, shell=True)

>>> count_lines('www.google.com')
'7\n'

```

(that output is correct, by the way - google does have 7 lines)

The function is insecure because it uses `shell=True`, which allows
[shell injection[(/shell_injection.md). A user to who instructs your
code to fetch the website `; rm -rf /` can do terrible things to your
machine.

If we naively convert the function to use `shell=False`, it doesn't
work.

```python
def count_lines(website):
    args = ['curl', website, '|', 'wc', '-l']
    return subprocess.check_output(args, shell=False)
>>> count_lines('www.google.com')
curl: (6) Could not resolve host: |
curl: (6) Could not resolve host: wc
Traceback (most recent call last):
  File "<stdin>", line 3, in count_lines
  File "/usr/lib/python2.7/subprocess.py", line 573, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
subprocess.CalledProcessError: Command 
'['curl', 'www.google.com', '|', 'wc', '-l']' returned non-zero exit status 6
```

The pipe doesn't mean anything special when shell=False, and so curl
tries to go download the website called pipe.

Fixed? No. More broken than before.

Ok, so we can't rely on pipes if we have shell=False, so how should we
do this?

### Correct

```python
def count_lines(website):
    args = ['curl', website]
    args2 = ['wc', '-l']
    p1 = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
    p2 = subprocess.Popen(args2, 
                          stdin=p1.stdout, stdout=subprocess.PIPE,
                          shell=False)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    return p2.communicate()[0]

>>> count_lines('www.google.com')
'7\n'
```

Now rather than calling a single shell process that runs each of our
programs, we run them separately ourselves. For the curl process, we
specify `stdout=subprocess.PIPE`, which tells subprocess to send that
output to the respective file handler.

Treat pipes like file descriptors (you can actually use FDs if you
want) - they may block on reading and writing if nothing is connected
to the other end. That's why we use `communicate()`, which reads until
EOF on the output and then waits for the process to terminate. You'll
generally want to avoid reading and writing to pipes directly unless
you really know what you're doing - it's easy to work yourself into a
situation that can deadlock.

Note that `communicate()` buffers the result in memory - if that's
not what you want, use a file descriptor for `stdout` to pipe that
output into a file.

## Consequences

* Using pipes helps you avoid shell injection in more complex situations
* It's possible to deadlock things with pipes (in Python or in shell)

## References

* https://docs.python.org/2/library/subprocess.html#subprocess.Popen.stdin
