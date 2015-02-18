
Cross-Site Request Forgery (CSRF)
==========================

Cross-Site Request Forgery occurs when sensitive web services have no protection to prevent attackers arbitrarily submitting data and commands. For example, an attacker may be able to cause an authorized user to submit form data to a web service which performs administrative functionality, or modifies personal settings.

To protect against this issue, a cryptographically secure nonce or hash must be included with each request, which must be verified prior to performing sensitive functionality.

### Correct
CSRF Token Example:
```html
<form method="POST" action="http://your.site/admin.do">
    <input type="hidden" name="action" value="some_privileged_action"/>
    <input type="hidden" name="CSRFToken" value="<token>"/>
    <input type="submit" name="submit" value="Do Some Privileged Action"/>
</form>
```

## Consequences

* Hijack of legitimate user sessions
* Access to privileged services and functionality
* Modification of protected data

## References

* [OWASP CSRF Guide](https://www.owasp.org/index.php/CSRF)
