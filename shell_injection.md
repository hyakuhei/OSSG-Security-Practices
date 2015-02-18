Subprocess Shell Injection
==========================

Let's start with one of the more common things we do: interacting
with the operating system.

We write a lot of code that configures, modifies, or otherwise
controls the system, and there are a number of pitfalls that can come
along with that.

Shelling out to another program is a pretty common thing to want to
do. Naturally, you'll want to pass parameters to this other program.

Here's a pretty simple little function for pinging another server.

### Incorrect
```python
def ping(myserver):
    return subprocess.check_output('ping -c 1 %s' % myserver, shell=True)

>>> ping('8.8.8.8')
64 bytes from 8.8.8.8: icmp_seq=1 ttl=58 time=5.82 ms
```

If the `myserver` parameter is user controlled, this can get ugly
pretty quickly.

This program just supplies a string as a command to the shell, which
runs the whole thing without thinking too hard about it. There's no
semantic separation between the input parameters.

It can't tell where the command is supposed to end, and where the
parameters start.

```python
>>> ping('8.8.8.8; rm -rf /')
64 bytes from 8.8.8.8: icmp_seq=1 ttl=58 time=6.32 ms
rm: cannot remove `/bin/dbus-daemon': Permission denied
rm: cannot remove `/bin/dbus-uuidgen': Permission denied
rm: cannot remove `/bin/dbus-cleanup-sockets': Permission denied
rm: cannot remove `/bin/cgroups-mount': Permission denied
rm: cannot remove `/bin/cgroups-umount': Permission denied
...
```

If you have malicious input, terrible things happen. Don't do this.

### Correct
Let's rewrite this function properly.
```python
def ping(myserver):
    args = ['ping', '-c', '1', myserver]
    return subprocess.check_output(args, shell=False)
```

Rather than passing a string to subprocess, our function passes a list
of strings. The ping program gets each argument separately (even if
the argument has a space in it), and the shell doesn't have to
(incorrectly) try and figure out what you meant.

(you don't have to explicitly set shell=False - it's the default)

Now, the ping command interprets the `myserver` value correctly as a
single argument, and complains because that's a really weird hostname
to try and ping.

```python
>>> ping('8.8.8.8; rm -rf /')
ping: unknown host 8.8.8.8; rm -rf /
```

This program is now much safer, even if it has to allow user-provided input.

## Consequences

* If you use shell=True, your code is extremely likely to be vulnerable
* Even if *your* code isn't vulnerable, the next person who maintains
  can easily introduce a vulnerability.
* Shell injections are arbitrary code execution - a competent attacker
  will use these to compromise the rest of your system.
