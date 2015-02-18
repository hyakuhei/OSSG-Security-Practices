
SQL Injection
=====================

Often we write code that writes or reads from a database based on some
parameters that are provided by the applications users. These parameters might
be credentials, resource identifiers or any other variable that the user
supplies to an application.

Care must be taken with how database queries are constructed so that they
cannot be subverted by an application user crafting malicious inputs. Such
inputs are referred to as injections, where the user causes a query to run that
has different consequences to those intended by the application developer.

The results of successful SQL injection attacks can range from disclosure of
information such as user passwords to gaining execution privileges and running
arbitrary commands on the database server.

SQL injection can typically be mitigated by using some combination of [prepared
statements](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet#Defense_Option_1:_Prepared_Statements_.28Parameterized_Queries.29)
, [stored procedures](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet#Defense_Option_2:_Stored_Procedures)
and [escaping](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet#Defense_Option_3:_Escaping_All_User_Supplied_Input)
of user supplied input. Most secure web applications will use all three and we
have described their use below.

### Incorrect
```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username = %s" % myvar
result = connection.execute(query)
for row in result:
    print "username:", row['username']
connection.close()
```

### Correct
A correct code example (SQLAlchemy):
```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username = :name"
result = connection.execute(query, name = myvar)
for row in result:
    print "username:", row['username']
connection.close()
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
A correct code example (MySQL):
```python
import MySQLdb

query = "select username from users where username = %s" % name
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(MySQLdb.escape_string(query))
```

### Incorrect
An incorrect code example (Postgesql (psycop2)):
```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select username from users where username = %s" % name)
```

### Correct
A correct code example (Postgesql (psycop2)):
Note that the standard python '%' operator is not used.
```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select username from users where username = %s", (name,))
```

## Consequences

* If you don't do this, Dracula will come for your head.
* Your eyes will fall out.
* Other Bad Things

## References

* https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet
