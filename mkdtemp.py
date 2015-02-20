import os
import tempfile

tmpdir = tempfile.mkdtemp()
predictable_filename = 'myfile'

# Ensure the file is read/write by the creator only
saved_umask = os.umask(0077)

path = os.path.join(tmpdir, predictable_filename)
print path
try:
    with open(path, "w") as tmp:
        tmp.write("secrets!")
except IOError as e:
    print 'IOError'
else:
    os.remove(path)
finally:
    os.umask(saved_umask)
    os.rmdir(tmpdir)
