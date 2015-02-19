Use secure channels for transmitting data
=====================

Data in flight over networks should be protected wherever possible. Although
some data may not appear to have strong confidentiality or integrity
requirements it is best practice to secure it.

When building any application that communicates over a network we should assume
that we do not control the network that the data travels over. We should
consider that the network may have hostile actors who will attempt to view or
change the data that we are transmitting.

### Clear Example
OpenStack API calls often contain credentials or tokens that are very sensitive
both from a confidentiality and integrity point of view. It is very important
that API calls be protected from malicious third parties viewing them or
tampering with their content - even for internal communications between
services on the same network.


### Less Obvious Example
Consider a server process that reports the current number of stars in the sky
and sends the data over the network to clients using a simple webpage. There's
no strong confidentiality requirements for this; the data isn't secret. However
integrity is important. An attacker on the network could alter the
communications going from the server to clients and for example, inject
browser exploits into the HTTP stream and compromising vulnerable clients.  

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

* A less knowledgeable deployer of OpenStack may inadvertently use unsecure
connections on a public network.

## References