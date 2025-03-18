from shutil import copy2
from os import path, stat, listdir, remove
from time import time, sleep
from sys import argv

init_dir = argv[1]
pathstack = [init_dir]
copy_dir = argv[2]
#copy_dir = '/storage/emulated/0/CODE/PY/file search/copy/'
searchterm = 'foo'
SEC_PER_YEAR = 31536000
counter = 0
print(argv)

# find and copy files
while len(pathstack) > 0:
    cur_dir = pathstack.pop(0)
    
    # check all items in cur_dir
    for item in listdir(cur_dir):
        cur_item = cur_dir + '/' + item
        
        if path.isdir(item):
            if item != 'copy':
                pathstack.insert(0, cur_item)
        elif searchterm in item:
            counter += 1
            print(f'Found {counter} file(s)', end='\r')
            copy2(cur_item, copy_dir)
print()
# delete files in copy_dir older than 1 year
counter = 0
for file in listdir(copy_dir):
    
    m_time = stat(copy_dir + file).st_mtime
    #if m_time + SEC_PER_YEAR < time():
    if m_time > 0:
        counter += 1
        remove(copy_dir + file)
        print(f'Deleted {counter} old file(s)', end='\r')
