
Validate certificates on HTTPS connections to avoid man-in-the-middle attacks
=====================

Ensure when developing a module that makes secure HTTPS connections, to use a library verifies certificates.  Many such libraries also provide an option to ignore certificate verification failures.  These options should be exposed to the OpenStack deployer to choose their level of risk.

Although the title of this guideline calls out HTTPS, verifying the identity of the hosts you are connecting to applies to most protocols (SSH, LDAPS, etc).

### Correct
A correct code example:
```python
import requests
requests.get('https://www.openstack.org/', verify=CONF.ca_file)
```

### Incorrect
```python
import requests
requests.get('https://www.openstack.org/', verify=False)
```

## Consequences

If the host's identity is not validated, your credentials can potentially be stolen.

* [OSSA-2014-005](http://security.openstack.org/ossa/OSSA-2014-005.html)

## References

* [OSSN-0033](https://wiki.openstack.org/wiki/OSSN/OSSN-0033)
* https://wiki.openstack.org/wiki/SecureClientConnections
