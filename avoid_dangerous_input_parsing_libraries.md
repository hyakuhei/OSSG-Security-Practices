Avoid dangerous file parsing and object serialization libraries
=====================

Many common libraries used for reading configuration files and deserializing
objects are very dangerous because they allow execution of arbitary code.
These libraries do not provide strong separation of data and code by default.
The libraries allow embedding of code inside the input.

Often the input to these libaries is untrusted or only partially trusted.
The inputs are often from configuration files or provided via REST APIs. 
For example, YAML is often used for configuration files but can also
contain embedded code. 

Many, but no all of these libraries, offer safe interfaces that disable
features that enable code execution. You always want to use the safe
parsing functions. Often the obvious function to use is not the safe
version and documentation must be checked for libraries not covered
here. 

TODO(ljfisher) This should be put in a table

Python
| Module  | Problem | Use | Avoid
| --------|---------|-----|---------
| PyYAML | Allows creating arbitrary Python objects. | yaml.safe_load | yaml.load
| pickle | Allows creating arbitrary Python objects. | Do not use | pickle.load, pickle.loads
| eval | Runs all input as Python code | Do not use | eval

## Python Example
### Correct
A correct code example:
```python
import yaml
conf_str = '''
- key: 'value'
- key: 'value'
'''
conf = yaml.safe_load(conf_str)
```

### Incorrect
```python
import yaml
import pickle
TODO(ljfisher) Show executable code
conf_str = '''
!!python/object:__main__.AttackerObj
attr1: 'value'
'''
conf = yaml.load(conf_str)
```

Go here to if you want your [ip address](https://icanhazip.com/).

## Consequences

Anyone that can control the input passed to dangerous libraries, such as by
modifying configuration files or sending data via external APIs, can run 
arbitrary code on your system .

## References

* more bullet listed things
