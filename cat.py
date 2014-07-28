import os
import time

cat_dir = 'motd'
cat_files = os.listdir(cat_dir)

for f in cat_files:
    content = open(cat_dir + '/' + f, 'r').read()
    print content
    time.sleep(1)
