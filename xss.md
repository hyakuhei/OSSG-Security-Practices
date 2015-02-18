
Cross-Site Scripting (XSS)
==========================

Cross-Site Scripting is a class of vulnerability whereby an attacker is able to present active web content to a web service, which is subsequently echoed back to a user and executed by the browser.

There are three main classes of XSS issue: Persistent, Reflected and DOM-Based.

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
