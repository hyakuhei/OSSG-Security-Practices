
Use oslo rootwrap conscientiously
=====================

Rootwrap provides a mechanism in which a caller may execute a command line with needed escalated privileges (typically as root).  Special care must be taken to ensure this use of code does not permit a lesser privileged user to run commands as root.

Rootwrap provides a series of filters to restrict command usage to limit the exposure.  The most commonly used filter is CommandFilter, but it also provides the least amount of restriction on how the command is called.

Consider the following before using rootwrap:
* Evaluate whether running the command as root is necessary.  In some cases, another user might be more appropriate.
* Try to avoid using rootwrap.  Look for Python native implementations of the required functionality rather than running operating system commands.
* If rootwrap is required, use the most restrictive filter possible (typically RegExpFilter).

### Incorrect
```python
# nova/virt/disk/vfs/localfs.py: 'chmod'
chmod: CommandFilter, chmod, root
```
This filter is too permissive because it allows the chmod command to be run as root with any number of arguments, on any file.

### Correct
A correct code example:
```python
# nova/virt/libvirt/utils.py: 'blockdev', '--getsize64', path
# nova/virt/disk/mount/nbd.py: 'blockdev', '--flushbufs', device
blockdev: RegExpFilter, blockdev, root, blockdev, (--getsize64|--flushbufs), /dev/.*
```

## Consequences

* A user of the API could potentially inject input that might be included in a call to rootwrap, thus causing chaos.

## References

* https://wiki.openstack.org/wiki/Rootwrap
