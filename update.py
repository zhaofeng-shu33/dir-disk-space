# core program to recursively scan the directory with some conditions
import os

def scan(data):
    # data: dic-like object
    # cur_dir: currently visited directory
    for i in os.listdir('./'):
        if data.get(i) is None:
            data[i] = {}
        if os.path.isdir(i):
            os.chdir(i)
            scan(data[i])
            os.chdir('../')
        else: # update file info in data
            data[i] = 512 * os.stat(i).st_blocks
