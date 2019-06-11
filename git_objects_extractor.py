import zlib
import os
from fnmatch import fnmatch

root = 'CHANGEME'
pattern = "*"

directories = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern): 
            if "pack" not in name:
                directories.append(os.path.join(path, name))

for directory in directories:
    compressed_contents = open(directory, 'rb').read()
    decompressed_contents = zlib.decompress(compressed_contents)
    print(decompressed_contents)
