
Unvalidated URL redirect
========================


It is common place for web forms to redirect to a different pages upon successful
submission of the form data. This is generally done by a using a _next_ parameter
in the http request. Any HTTP parameter is user controlled input, and can be
abused by attackers to redirect a user to a malicious site. This is commonly
used in phishing attacks. An example of how an attacker may exploit URL redirects: https://www.example.com/login.php?next=http://attacker.com/phonylogin.php

To counter this type of attack redirects need to be validated before redirecting the user to an external site. Essentially you should confirm that the redirection will take the user to another page within your site.


### Correct

The following is an example using the Flask web framework. It essentially
check that the URL the user is being redirected to originates from the
same host as the host serving the content.  

```python

from flask import request, g, redirect
from urlparse import urlparse, urljoin


def is_safe_redirect_url(target):
  host_url = urlparse(request.host_url)
  redirect_url = urlparse(urljoin(request.host_url, target))
  return redirect_url.scheme in ('http', 'https') and \
    host_url.netloc == redirect_url.netloc


def get_safe_redirect():
  url =  request.args.get('next')
  if url and is_safe_redirect_url(url):
    return url

  url = request.referrer
  if url and is_safe_redirect_url(url):
    return url

  return '/'

```

The Django framework contains a [django.utils.http.is_safe_url](https://github.com/django/django/blob/93b3ef9b2e191101c1a49b332d042864df74a658/django/utils/http.py#L268) function that can
be used to validate redirects without implementing a custom version.



### Incorrect



```python

import os
from flask import Flask,redirect, request

app = Flask(__name__)

@app.route('/')
def example_redirect():
    return redirect(request.args.get('next'))

```

## Consequences

Unvalidated redirects can make your site a target for phishing attacks that can
lead to users credentials being stolen.


* [OSSA-2012-012](http://security.openstack.org/ossa/OSSA-2012-012.html)


## References

* [CWE-601: URL Redirection to Untrusted Site](http://cwe.mitre.org/data/definitions/601.html)
* [OWASP Top 10 2013 - Unvalidated redirects and forwards ](https://www.owasp.org/index.php/Top_10_2013-A10-Unvalidated_Redirects_and_Forwards)
