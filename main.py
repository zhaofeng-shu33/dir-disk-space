import argparse
from time import time
import os

from structure import load_cache
from structure import save_cache
from structure import get_total_size 
from update import scan
import update

if __name__ == '__main__':
    update.current_timestamp = time()
    parser = argparse.ArgumentParser()
    parser.add_argument('--cache_filename', default='data.json')
    parser.add_argument('--dir', default='./')
    args = parser.parse_args()
    data = {}
    current_dir = os.getcwd()
    os.chdir(args.dir)
    scan(data)
    os.chdir(current_dir)
    save_cache(args.cache_filename, data)
    print(get_total_size(data) / 1024, 'KB') 
