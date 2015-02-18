ToDo (31):
* bad protocols: 'PROTOCOL_SSLv2', 'SSLv2_METHOD', 'SSLv23_METHOD', 'PROTOCOL_SSLv3', 'PROTOCOL_TLSv1', 'SSLv3_METHOD', 'TLSv1_METHOD'
* pickle: "Pickle library appears to be in use, possible security issue."
* md5: "Use of insecure MD5 hash function."
* subprocess_popen:"Use of possibly insecure system call function (subprocess.Popen)."
* subprocess_call:"Use of possibly insecure system call function (subprocess.call)."
* os_popen: "Use of insecure / deprecated system call function (os.popen)."
* os_startfile_q: "Use of insecure system function (os.startfile)."
* mktemp_q: "Use of insecure and deprecated function (mktemp)."
* eval:"Use of possibly insecure function - consider using safer ast.literal_eval."
* mark_safe: "Use of mark_safe() may expose cross-site scripting vulnerabilities and should be reviewed."
* httpsconnection: "Use of HTTPSConnection does not provide security, see https://wiki.openstack.org/wiki/OSSN/OSSN-0033"
* urllib_urlopen: "Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected."
* telnet: "Telnet is considered insecure. Use SSH or some other encrypted protocol."
* pickle, subprocess, Crypto: "Consider possible security implications associated with {module} module."
* Use of random is not suitable for security cryptographic purposes (INFO): plugins/crypto_random.py
* Random library should not be used for any security or cryptographic purposes (INFO): plugins/crypto_random.py
* Possible SQL injection vector through string-based query construction, without SQLALCHEMY use (WARNING): plugins/injection_sql.py
* Possible SQL injection vector through string-based query contruction (INFO): plugins/injection_sql.py
* 'ssl.wrap_socket call with no SSL/TLS protocol version specified, the default SSLv23 could be insecure, possible security issue.  %s' % context.call_args_string) (INFO): plugins/insecure_ssl_tls.py
* 'ssl.wrap_socket call with insecure SSL/TLS protocol version identified, security issue.  %s' % context.call_args_string (ERROR): plugins/insecure_ssl_tls.py
* 'SSL.Context call with insecure SSL/TLS protocol version identified, security issue.  %s' % context.call_args_string) (ERROR): plugins/insecure_ssl_tls.py
* 'Function call with insecure SSL/TLS protocol identified, possible security issue.  %s' % context.call_args_string) (WARN): plugins/insecure_ssl_tls.py
* 'function definition identified with insecure' ' SSL/TLS protocol version by default, possible security' ' issue.  %s' % context.call_args_string) (WARN): plugins/insecure_ssl_tls.py
* 'Possible binding to all interfaces' (WARN): plugins/general_bind_all_interfaces.py
* "Possible hardcoded password '(%s)'" % word (WARN): plugins/general_hardcoded_password.py
* "Probable insecure usage of temp file/directory" (WARN): plugins/general_hardcoded_tmp.py
* 'Popen call with shell=True identified, security issue.  %s' % context.call_args_string) (ERROR): plugins/injection_shell.py
* 'Function call with shell=True parameter identified, possible security issue.  %s' % context.call_args_string) (WARN): plugins/injection_shell.py
* 'Requests call with verify=False disabling SSL certificate checks, security issue.   %s' % context.call_args_string) (ERROR): plugins/crypto_request_no_cert_validation.py
* Use of exec detected: plugins/exec.py
* 'Chmod setting a permissive mask %s on ' 'file (%s).' % (oct(mode), filename)) (ERROR): plugins/general_bad_file_permissions.py
* 'Possible wildcard injection ' 'in call: %s' % context.call_function_name_qual) (ERROR): plugins/injection_wildcard.py

Done:
* os_exec: "Use of possibly insecure system call function (os.exec or os.spawn)."
* yaml_load: "Use of unsafe yaml load. Allows instantiation of arbitrary objects. Consider yaml.safe_load()."
