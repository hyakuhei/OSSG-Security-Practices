Avoid dangerous file parsing and object serialization libraries (YAML, pickle)
=====================

Many common libraries (PyYAML, pickle) we often use for reading configuration files and deserializing
objects are very dangerous because they allow execution of arbitrary code.
These libraries do not provide strong separation of data and code by default and allow embedding of code inside the input.

Often the input to these libraries is untrusted or only partially trusted.
These unsafe inputs can come from configuration files or provided via REST APIs.
For example, we often use YAML for configuration files but YAML files can also
contain embedded Python code. An administrator may be able to modify a
configuration file but not not always act as the service reading the
configuration file. We shouldn't assume configuration files can only be
modified by root.

Many, but not all, of these libraries, offer safe interfaces that disable
features that enable code execution. You always want to use the safe functions
to load input. Often the obvious function to use is not the safe
one and we should check the  documentation for libraries not covered
here.

### Python Libraries

We often use YAML, pickle, or eval to load data into our Python programs,
but this is dangerous. PyYAML has a safe way to load code, but pickly and
eval do not. 

| Module   | Problem   |  Use  | Avoid
| -------- | --------- | ----- | ---------
| PyYAML | Allows creating arbitrary Python objects. | yaml.safe_load | yaml.load
| pickle | Allows creating arbitrary Python objects. | Do not use | pickle.load, pickle.loads
| eval | Runs all input as Python code | Do not use | eval

## Python Example
### Correct

Here we use PyYAMLs safe YAML loading function:
```python
import yaml
conf_str = '''
- key: 'value'
- key: 'value'
'''
conf = yaml.safe_load(conf_str)
```

### Incorrect

yaml.load is the obvious function to use but is dangerous:
```python
import yaml
import pickle
TODO(ljfisher) Show executable code
conf_str = '''
!!python/object:__main__.AttackerObj
key: 'value'
'''
conf = yaml.load(conf_str)
```

## Consequences

Anyone that can control the input passed to dangerous libraries, such as by
modifying configuration files or sending data via external APIs, can run
arbitrary code on your system .

## References

* [PyYAML: Loading YAML](http://pyyaml.org/wiki/PyYAMLDocumentation#LoadingYAML)
