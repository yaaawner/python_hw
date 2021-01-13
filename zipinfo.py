import sys
import io
import zipfile
b = str()

for line in sys.stdin:
    if line[-1] == '\n':
        b += line[:-1]
    else:
        b += line

f = io.BytesIO(bytes.fromhex(b))
z = zipfile.ZipFile(f)
files = [i for i in z.namelist() if i[-1] != '/']

size = 0
for i in files:
    size += z.getinfo(i).file_size

print(len(files), size)