
Prefer an encrypted connection as the default
=====================

Protocol options should default to the secure alternative.  The prime example is using HTTPS instead of HTTP.

### Correct
A correct code example:
```python
cfg.StrOpt('protocol',
           default='https',
           help='Default protocol to use when connecting to glance.'),
```

### Incorrect
```python
cfg.StrOpt('protocol',
           default='http',
           help='Default protocol to use when connecting to glance.'),
```


## Consequences

* A less knowledgable deployer of OpenStack may inadvertently use unsecure connections on a public network.

## References
