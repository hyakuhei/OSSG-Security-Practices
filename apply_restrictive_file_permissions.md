
Apply Restrictive File Permissions
==================================

Files should be created with restrictive file permissions to prevent vulnerabilities such as information disclosure and code execution.  

In particular, any files which may contain confidential information should be set to only permit access by the owning user and group (no world/others access).

Discretion should be used when granting write access to files such as configuration files to prevent vulnerabilities including denial of service and remote code execution.

### Correct
Consider the configuration file for a service "secureserv" which configuration including passwords in "secureserv.conf".  Since it contains sensitive information, other users should not be given access.

```sh
ls -l secureserv.conf
-rw-------   1 secureserv  secureserv   6710 Feb 17 22:00 secureserv.conf
```

To set the file permissions as shown above, run the following command in Linux:

```sh
chmod 0600 secureserv.conf
```

Note that it is also important to verify the owner and group of the file.  It is particularly important to note what other users are part of a group that you give access to.  The best practice is that if group access it not needed, don't grant it.  This is part of the principle of least privilege.

### Incorrect
Consider the same example config file in the above example with the following permissions:

```sh
ls -l secureserv.conf
-rw-rw-rw-   1 secureserv  secureserv   6710 Feb 17 22:00 secureserv.conf
```

Here the file permissions are set to 666 (read and write access for owner, group, and others).  This creates several vulnerabilities as described below.

## Consequences

* Reading passwords from the config file
A malicious user can read sensitive information (such as passwords) from the file.

* Setting a new password
A malicious user can write a new password into the file, potentially granting access.

* Code execution
If the config file stores commands or parameters, for example, a malicious user can tamper with the config file to achieve code execution.

* Denial of service
An attacker can delete the contents of the file to prevent the service from running properly.

## References

* File system controls should be implemented according to [least privilege](http://en.wikipedia.org/wiki/Principle_of_least_privilege).

* More information about setting securing file system permissions in Linux can be found [here](http://www.linuxsecurity.com/docs/SecurityAdminGuide/SecurityAdminGuide-8.html).
