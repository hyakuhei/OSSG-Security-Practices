
Cross-Site Scripting (XSS)
==========================

Cross-Site Scripting is a class of vulnerability whereby an attacker is able to present active web content to a web service, which is subsequently echoed back to a user and executed by the browser.

There are three main classes of XSS issue: Persistent, Reflected and DOM-Based. Persistent XSS issues are those where user input is stored by the server, either in a database or server files, which is later presented to any user visiting the affected web page. Reflected XSS issues are those where user input in a request is immediately reflected to the user without sanitization. DOM-Based issues are less common, and are present in web applications with rich client-side JavaScript clients which generate dynamic code or web content using user controllable data (i.e. URL parameters).

### Incorrect
```php
$name = $_GET['name'];

echo("Hello ".name);
```

### Correct
Reflected XSS PHP example:
```php
$name = htmlspecialchars($_GET['name']);

echo("Hello ".$name);
```

## Consequences

* Hijack of legitimate user sessions
* Disclosure of sensitive information
* Access to privileged services and functionality
* Delivery of malware and browser exploits from our trusted domain

## References

* [OWASP XSS Guide](https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29)
