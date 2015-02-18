Use Strong and Established Cryptographic Elements
=================================================

Cryptography is a complicated topic and the area of significant debate. The specifics mentioned in this guide are likely to change as state of the art continues to advance.

We try to follow two general rules in the OpenStack context:
* Established, reputable libraries should be used where cryptographic functionality is required.
* When utilizing cryptographic hashing, signing, or encryption, strong cryptographic primitives should be used.

The Python cryptography libraries currently in OpenStack global requirements include [PyCrypto](https://www.dlitz.net/software/pycrypto/), [pyOpenSSL](https://github.com/pyca/pyopenssl), [cryptography](https://cryptography.io/), and [passlib](https://pythonhosted.org/passlib/).

Use of the following cryptographic elements is encouraged:
* SHA-256 is the preferred hashing algorithm.
* AES is the preferred general encryption algorithm, with 128, 192 or 256 bit key lengths.
* *TBD - alg. for password encryption?*
* HMAC is the preferred signing construction, in conjunction with a preferred hashing algorithm.
* TLSv1.1 or TLSv1.2 are preferred for protecting data in transit between client and web service.

While for some use cases it may seem appropriate to use a weaker cryptographic element, the options listed above are generally advised. Usage of the following is discouraged:
* MD5
* SSLv2, SSLv3, TLSv1.0

## Consequences

* Weak cryptographic elements may be vulnerable to various types of attack, ultimately affecting confidentiality and integrity of the associated system or dataset at risk.

## References

* [OWASP Guide to Cryptography](https://www.owasp.org/index.php/Guide_to_Cryptography)
* [NSA Suite B Cryptography](https://www.nsa.gov/ia/programs/suiteb_cryptography/index.shtml)
* [NIST Cryptographic Toolkit](http://csrc.nist.gov/groups/ST/toolkit/)
* [Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS)
