
SQL Injection
=====================

Often we write code that interacts with a database using parameters provided by
the applications users. These parameters might be credentials, resource
identifiers or any other user-supplied data.

Care must be taken when dynamically creating database queries so they cannot be
subverted by user crafted malicious input. Such inputs are referred to as SQL
injections, where the user input changes the logic of the SQL query, which
results in behavior not intended by the application developer.

The results of a successful SQL injection attack can include disclosure of
sensitive information, such as user passwords, modification or deletion of
important data, and gaining execution privileges allowing an attacker to run
arbitrary commands on the database server.

SQL injection can typically be mitigated by using some combination of [prepared
statements](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet#Defense_Option_1:_Prepared_Statements_.28Parameterized_Queries.29)
, [stored procedures](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet#Defense_Option_2:_Stored_Procedures)
and [escaping](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet#Defense_Option_3:_Escaping_All_User_Supplied_Input)
of user supplied input. Most secure web applications will use all three and we
have described their use below.

##Code Examples
###SQLAlchemy

#### Incorrect

This example uses python's built in parameter substitution mechanism '%' to
insert a value into the query string, this will perform an unsafe literal
insertion and not provide any escaping.

```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username = '%s'" % myvar
result = connection.execute(query)
for row in result:
    print "username:", row['username']
connection.close()
```

#### Correct

This example uses SQLAlchemy's built in parameter substitution mechanism to
safely replace the ':name' variable with a provided value.

```python
import sqlalchemy

connection = engine.connect()
query = "select username from users where username = :name"
result = connection.execute(query, name = myvar)
for row in result:
    print "username:", row['username']
connection.close()
```

### MySQL
#### Incorrect

Without using any escaping mechanism, potentially unsafe queries can be
created.

```python
import MySQLdb

query = "select username from users where username = '%s'" % name
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(query)
```

#### Correct

In this example the query is created using pythons standard, unsafe '%'
operator. MySQL's 'escape_string' method is used to perform escaping on the
query string immediately before executing it.

```python
import MySQLdb

query = "select username from users where username = '%s'" % name
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(MySQLdb.escape_string(query))
```

An alternative, but also correct, way to do this using a parameterised query
might look like the following:

```python
import MySQLdb

query = "select username from users where username = '%s'"
con = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    cur = con.cursor()
    cur.execute(query, (username_value,))
```

### PostgreSQL (Psycop2)
#### Incorrect

This example uses python's unsafe default parameter substitution mechanism
to build a query string. This will not perform any escaping, unlike the correct
example below the string is processed and passed as a single parameter to
'execute'

```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select username from users where username = '%s'" % name)
```

#### Correct

This example uses Psycop2's parameter substitution mechanism to build a query
string. Despite the use '%' to indicate the substitution token, it is not the
same as pythons built in string operator %. Note the value(s) are passed as
parameters to 'execute' separately.

```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select username from users where username = '%s'", (name,))
```

## Consequences

* If you don't do this, Dracula will come for your head.
* Your eyes will fall out.
* Other Bad Things

## References

* https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet
