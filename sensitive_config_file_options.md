
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

If an option is not marked secret and the logger debug flag is activated, that sensitive information would appear in the logs.

### Example Log Entries
```
2015-02-18 20:46:48.928 25351 DEBUG nova.openstack.common.service [-] Full set of CONF: _wait_for_exit_or_signal /usr/lib/python2.7/dist-packages/nova/openstack/common/service.py:166
2015-02-18 20:46:48.937 25351 DEBUG nova.openstack.common.service [-] Configuration options gathered from: log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:1982
2015-02-18 20:46:51.482 25351 DEBUG nova.openstack.common.service [-] host.ip                 = 127.0.0.1 log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:2002
2015-02-18 20:46:51.491 25351 DEBUG nova.openstack.common.service [-] host.port               = 443 log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:2002
2015-02-18 20:46:51.502 25351 DEBUG nova.openstack.common.service [-] host.username           = root log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:2002
2015-02-18 20:46:51.486 25351 DEBUG nova.openstack.common.service [-] host.password           = SuperSecretPassword log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:2002
```

## References

* http://docs.openstack.org/developer/oslo.config/cfg.html#special-handling-instructions
* https://review.openstack.org/#/c/138944
