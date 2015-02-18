Create, use, and remove temporary files securely
=====================

Often we want to create temporary files to save data that we can't hold
in memory or to pass to external programs that must read from a file.
The obvious way to do so is to generate a unique file name in a common
system tempory directory such as /tmp. This still leaves us open to a
number of dangerous issues. Our unique file name must also be unpredictable.
The file must be opened such that it will fail if an existing file has
the same name. We must make sure the file has the correct permissions.
We have to assess if we care if others can know about our tempoary
file. Finally, we must cleanup the tempoary file when we no longer
need it.

If we don't take all these precautions we open ourselves up to a number
of dangerous security problems. Malicious users that can predict the
file name can effectly hijack the file and do all sorts of bad things.

TODO(ljfisher) finish this


### Correct
A correct code example:
```python
import subprocess
subprocess.POpen('rm -rf /', shell=True)
```

### Incorrect
```python
0/0
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
