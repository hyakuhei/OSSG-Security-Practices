
Ensure sensitive config file options are marked secret to prevent disclosure in logs
=====================

The oslo.config library provides a mechanism to sanitize sensitive information contained in config files.  It will only mask out this information if the config option is marked with 'secret=True' where it is defined.

### Correct
A correct code example:
```python
 cfg.StrOpt('password',
            help='Password of the host.',
            secret=True),
```

### Incorrect
```python
 cfg.StrOpt('password',
            help='Password of the host.'),
```

## Consequences

* Sensitive information contained in config files will be leaked into logs

## References

* http://docs.openstack.org/developer/oslo.config/cfg.html#special-handling-instructions
* https://review.openstack.org/#/c/138944
