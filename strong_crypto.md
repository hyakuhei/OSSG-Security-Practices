Use Strong and Established Cryptographic Elements
=================================================

Cryptography is a complex topic, frequently miss-understood, and it is
the area of significant debate. The specifics mentioned in this guide
are likely to change as state of the art continues to advance.

In general, you should follow some simple rules for using cryptography:
* Do not invent your own cryptography, use existing algorithms and
implementations.
* When utilizing cryptographic hashing, signing, or encryption, strong
cryptographic primitives must be used.
* Use established, reputable libraries with active maintenance in
preference to implementing your own algorithms.
* Pay carefull attention to key management and distribution, this is
generally a harder problem than algorithm selection and implementation.

Cryptography should be used to solve a specific problem or mitigate a
specific threat, such as ensuring the confidentiality of some data in
transit over an un-trusted network connection. Both the cryptographic
algorithm and the key strength should be appropriate for the threat you
are trying to mitigate with the encryption, and the limitations of the
cryptography should be understood. For example, if encryption is
applied to a network link, it will not protect the data when it is
processed or stored at either end of that link. When deploying
cryptography, the impact to system performance and availability must
also be considered.

The Python cryptography libraries currently in OpenStack global requirements include [PyCrypto](https://www.dlitz.net/software/pycrypto/), [pyOpenSSL](https://github.com/pyca/pyopenssl), [cryptography](https://cryptography.io/), and [passlib](https://pythonhosted.org/passlib/).

Use of the following cryptographic elements is encouraged:
* SHA-256 is the preferred hashing algorithm.
* AES is the preferred general encryption algorithm, with 128, 192 or
256 bit key lengths.
* *TBD - alg. for password encryption?*
* HMAC is the preferred signing construction, in conjunction with a
preferred hashing algorithm.
* TLSv1.2 or TLSv1.1 are preferred for protecting data in transit
between clients and web services, but they must be configured securely,
certificate validity, expiry and revocation status must be checked.

While for some use cases it may seem appropriate to use a weaker
cryptographic element, the options listed above are generally advised.
Usage of the following is strongly discouraged:
* MD5
* DES
* RC4
* SSLv2, SSLv3, TLSv1.0

## Consequences

* Weak cryptographic elements may be vulnerable to various types of
attack, ultimately affecting confidentiality and integrity of the
associated system or dataset at risk.

## References

* [OWASP Guide to Cryptography](https://www.owasp.org/index.php/Guide_to_Cryptography)
* [NSA Suite B Cryptography](https://www.nsa.gov/ia/programs/suiteb_cryptography/index.shtml)
* [NIST Cryptographic Toolkit](http://csrc.nist.gov/groups/ST/toolkit/)
* [Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS)
