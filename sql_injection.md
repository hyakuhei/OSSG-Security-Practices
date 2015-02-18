
SQL Injection
=====================

SQL Injection is a class of vulnerability that allows an attacker to create
malicious program inputs that result in undesirable SQL queries being
constructed and executed against a database. The results of successful SQL
injection attacks can range from disclosing information to gaining execution
privileges on the database server.

Some other paragraph

## Code Examples
### SQLAlchemy
#### Correct

This example uses SQLAlchemy's built in parameter substitution mechanism to
safely replace the ':name' variable with a provided value.

```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username == :name"
result = connection.execute(query, name = myvar)
for row in result:
    print "username:", row['username']
connection.close()
```

#### Incorrect

This example uses python's built in parameter substitution mechanism '%' to
insert a value into the query string, this will perform an unsafe literal
insertion and not provide any escaping.

```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username == %s" % myvar
result = connection.execute(query)
for row in result:
    print "username:", row['username']
connection.close()
```

### MySQL
#### Correct

In this example the query is created using pythons standard, unsafe '%'
operator. MySQL's 'escape_string' method is used to perform escaping on the
query string immediately before executing it.

```python
import MySQLdb

query = "select username from users where username == %s" % name
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(MySQLdb.escape_string(query))
```

#### Incorrect

Without using any escaping mechanism, potentially unsafe queries can be
created.

```python
import MySQLdb

query = "select username from users where username == %s" % name
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(query)
```

### Postgresql (Psycop2)
#### Correct

This example uses Psycop2's parameter substitution mechanism to build a query
string. Despite the use '%' to indicate the substitution token, it is not the
same as pythons built in string operator %, note the value(s) are passed as
parameters to 'execute' separately.

```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select username from users where username == %s", (name,))
```

#### Incorrect

This example uses python's unsafe default parameter substitution mechanism
to build a query string. This will not perform any escaping, unlike the correct
example above the string is processed and passed as a single parameter to
'execute'

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
