
Cross-Site Scripting (XSS)
==========================

Cross-Site Scripting is a class of vulnerability whereby an attacker is able to present active web content to a web service, which is subsequently echoed back to a user and executed by the browser.

There are three main classes of XSS issue: Persistent, Reflected and DOM-Based. Persistent XSS issues are those where user input is stored by the server, either in a database or server files, which is later presented to any user visiting the affected web page. Reflected XSS issues are those where user input in a request is immediately reflected to the user without sanitization. DOM-Based issues are less common, and are present in web applications with rich client-side javascript clients which generate dynamic code or web content using user controllable data (i.e. URL parameters).

### Correct
A correct code example:
```python
import subprocess
subprocess.POpen('rm -rf /', shell=True)
```

### Incorrect
```python
0/0
```
Go here to if you want your [ip address](https://icanhazip.com/).

## Consequences

* If you don't do this, Dracula will come for your head.
* Your eyes will fall out.
* Other Bad Things

## References

* more bullet listed things
