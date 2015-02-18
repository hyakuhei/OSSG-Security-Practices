
Path Traversal
==============

A path traversal attack is when an attacker supplies input that is used directly to access a file on the file system. The input usually attempts to break out of the applications working directory and access a file elsewhere on the file system.
This category of attack can be mitigated by restricting the scope of file system access and reducing attack surface by using a restricted file permission profile.


### Correct


The following example demonstrates how you can use python code to restrict
access to files within a specific directory. This can be used as a mechanism
to defeat path traversal.

```python

import os
import sys

def is_safe_path(basedir, path, follow_symlinks=True):
  # resolves symbolic links
  if follow_symlinks:
    return os.path.realpath(path).startswith(basedir)

  return os.path.abspath(path).startswith(basedir)


def main(args):
    for arg in args:
        if is_safe_path(os.getcwd(), path):
            print("safe: {}".format(arg))
        else:
            print("unsafe: {}".format(arg))

if __name__ == "__main__":
    main(sys.argv[1:])

```


### Incorrect

Path traversal flaws also can happen when unpacking a compressed archive of files. An example of where this has happened within OpenStack is [OSSA-2011-001]((http://security.openstack.org/ossa/OSSA-2011-001.html). In this
case a tar file from an untrusted source could be unpacked to overwrite files
on the host operating system.

```python

import tarfile

def untar_image(path, filename):
    tar_file = tarfile.open(filename, 'r|gz')
    tar_file.extract_all(path)
    image_file = tar_file.get_names()[0]
    tar_file.close()
    return os.path.join(path, image_file)


```

## Consequences

The impact of not validating file paths essentially allows the attacker to read
or write to any file that the application can which can lead to information
leakage and can be used to pivot to other more serious attacks like remote
code execution.


* [OSSA-2011-001](http://security.openstack.org/ossa/OSSA-2011-001.html)
* [OSSA-2014-041](http://security.openstack.org/ossa/OSSA-2014-041.html)
* [OSSA-2015-002](http://security.openstack.org/ossa/OSSA-2015-002.html)

## References

* [CWE-22: Improper Limitation of a Pathname to a Restricted Directory](http://cwe.mitre.org/data/definitions/22.html)
