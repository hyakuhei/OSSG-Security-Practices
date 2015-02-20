Create, use, and remove temporary files securely
=====================

Often we want to create temporary files to save data that we can't hold
in memory or to pass to external programs that must read from a file.
The obvious way to do so is to generate a unique file name in a common
system temporary directory such as /tmp. This still leaves us open to a
number of dangerous issues. Our unique file name must also be unpredictable.
The file must be opened such that it will fail if an existing file has
the same name. We must make sure the file has the correct permissions.
We have to assess if we care if others can know about our tempoary
file. Finally, we must cleanup the tempoary file when we no longer
need it.

If we don't take all these precautions we open ourselves up to a number
of dangerous security problems. Malicious users that can predict the
file name and write to directory containing the temporary file can
effectively hijack the temporary file by creating a symlink with the
name of the temporary file before the program does so itself.
This allows a malicious user to supply malicious data or cause actions
by the program to affect attacker chosen files. The references
have more extensive descriptions of potential dangers.

Most programming lanuages provide functions to create temporary
files. However, many of these functions are unsafe and should not
be used. We need to be careful to use the safe functions.

Despite the safer temporary file creation APIs we must still be
aware of where we are creating tempory files. Generally, temporary
files should always be created on the local filesystem. Many
remote filesystems (for example, NFSv2) do not support the open
flags needed to safely create tempoary files.

### Python

Use | Avoid
----- | -----
tempfile.TemporaryFile        | tempfile.mktemp
tempfile.NamedTemporaryFile   | open
tempfile.SpooledTemporaryFile |
tempfile.mkstemp              |
tempfile.mkdtemp              |

tempfile.TemporaryFile should be used whenever possible. Besides
creating temporary files safely it also hides the file and cleans up
the file automatically.

### Incorrect

Creating temporary files with predictable paths leaves them open to time of
check, time of use attacks (TOCTOU). Given the following code snippet an
attacker might pre-emptively place a file at the specified location.

```python
import os
import tempfile

def dont_use_predictable_paths(filename):

    tmp = os.path.join(tempfile.gettempdir(), filename)
    if not os.path.exists(tmp):
        with open(tmp, "w") file:
            file.write("defaults")

    # create a file like this you cannot be certain of
    # the integrity of its contents

```


There is also an insecure method within the Python standard library that
cannot be used in a secure way to create temporary file creation.


```python
import os
import tempfile
def dont_use_mktemp(prefix):
    return open(tempfile.mktemp(), "w")
```

Finally there are many ways developers try to create a secure filename,
however if the attacker is skilled enough mechanisms like the following
are easily defeated.

```python

def dont_invent_naming_convention():
    filename = "{}/{}.tmp".format(tempfile.gettempdir(), os.getpid())
    return open(filename, "w")

```

### Correct

The Python standard library provides a number of secure ways at creating temporary files and directory. The following are examples of how you can use them.

Creating files:

```python
import os
import tempfile

def using_TemporaryFile_context_manager_for_clean_up():
    with tempfile.TemporaryFile() as tmp:
        go_do_stuff(tmp)

def using_NamedTemporaryFile():
    tmp = tempfile.NamedTemporaryFile(delete=True)
    go_do_stuff(tmp)
    tmp.close()  # deletes the file

def using_mkstemp_to_create_a_tempfile(**kwargs):
    fd, path = tempfile.mkstemp(**kwargs)
    try:
        with os.fdopen(fd, mode="w") as tmp:
            # do stuff with temp file
            tmp.write("secrets!")

    finally:
        os.remove(path)


```

We can also safely create a temporary directory and create our tempory files
with predictable names inside it. We use os.open because it allows us to 
explicitly set the file permissions of the new file. We could use open, but
then must deal with temporarily modifying the umask.

```python

TODO(ljfisher) check this actually works

def using_mkdtemp_to_create_directories(predictable_filename):
    tmpdir = tempfile.mkdtemp()

    try:
        fd = os.open(os.join(tmpdir, predictable_filename), os.O_RDWR | os.CREAT) 
        with os.fdopen(fd, 'w') as tmp:
            tmp.write("secrets!")
    finally:
        if fd:
            os.unlink(fd)
    

def using_mkdtemp_to_create_directories(predictable_filename):
    tmpdir = tempfile.mkdtemp()
    saved_umask = os.umask(077)
    try:
        with open(os.join(tmpdir, predictable_filename), "w") as tmp:
            tmp.write("secrets!")

    finally:
        os.umask(saved_umask)

    return tmpdir
```

## Consequences

* The program can be tricked into performing file actions against the
wrong file or using a malicious file instead of the expected temporary
file

## References
* [Temporary File - CERT Secure Coding Standards](https://www.securecoding.cert.org/confluence/download/attachments/3524/07.5+Temporary+Files+v2.pdf)
* [FIO21-C. Do not create temporary files in shared directories](https://www.securecoding.cert.org/confluence/display/seccode/FIO21-C.+Do+not+create+temporary+files+in+shared+directories)
* [FIO03-J. Remove temporary files before termination](https://www.securecoding.cert.org/confluence/display/java/FIO03-J.+Remove+temporary+files+before+termination)
* [CWE-377: Insecure Temporary File](http://cwe.mitre.org/data/definitions/377.html)
* [CWE-379: Creation of Temporary File in Directory with Incorrect Permissions](http://cwe.mitre.org/data/definitions/379.html)
* [CWE-459: Incomplete Cleanup](http://cwe.mitre.org/data/definitions/459.html)
* [Python tempfile](https://docs.python.org/2/library/tempfile.html)
