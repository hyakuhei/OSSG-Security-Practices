
SQL Injection
=====================

SQL Injection is a class of vulnerability that allows an attacker to create
malicious program inputs that result in undesirable SQL queries being
constructed and executed against a database. The results of successful SQL
injection attacks can range from disclosing information to gaining execution
privileges on the database server.

Some other paragraph

### Correct
A correct code example (SQLAlchemy):
```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username == :name"
result = connection.execute(query, name = myvar)
for row in result:
    print "username:", row['username']
connection.close()
```

### Incorrect
```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username == %s" % myvar
result = connection.execute(query)
for row in result:
    print "username:", row['username']
connection.close()
```

### Correct
A correct code example (MySQL):
```python
import MySQLdb

query = "select username from users where username == %s" % name
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(MySQLdb.escape_string(query))
```

### Incorrect
An incorrect code example (MySQL):
```python
import MySQLdb

query = "select username from users where username == %s" % name
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(query)
```

### Correct
A correct code example (Postgesql (psycop2)):
Note that the standard python '%' operator is not used.
```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select username from users where username == %s", (name,))
```

### Incorrect
An incorrect code example (Postgesql (psycop2)):
```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select username from users where username == %s" % name)
```

## Consequences

* If you don't do this, Dracula will come for your head.
* Your eyes will fall out.
* Other Bad Things

## References

* more bullet listed things
