
SQL Injection
=====================

Put your description here.

Separate your paragraphs with a blank line.

### Correct
A correct code example (SQLAlchemy):
```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where"
result = connection.execute("select username from users where")
for row in result:
    print "username:", row['username']
connection.close()

SQLAlchemy connection.execute(query, name = myvar)
```

A correct code example (MySQL):
```python
import subprocess
subprocess.POpen('rm -rf /', shell=True)
```

A correct code example (Postgesql (psycop2)):
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
