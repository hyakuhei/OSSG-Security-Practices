
Safe use of oslo rootwrap
=====================

Rootwrap provides a mechanism in which a caller may execute a command line with needed escalated privileges (typically as root).  Special care must be taken to ensure this use of code does not permit a lessor privileged user from the API gaining access to run commands as root.

Rootwrap provides a series of filters to restrict the command to limit the exposure.  The most commonly used filter is CommandFilter, but it also provides the least amount of restriction on how the command is called.

Consider the following before using rootwrap:
* Try to avoid using rootwrap.  Look for alternative libraries that might provide the functionality with root permission.
* Use the most restrictive filter possible, typically RegExpFilter.
* Evaluate whether running the command as root is necessary.  In some cases, another user might be more appropriate.

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

* A user of the API could potentially inject input that might be included in a call to rootwrap, thus causing caos.

## References

* https://wiki.openstack.org/wiki/Rootwrap
