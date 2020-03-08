from time import time
from update import current_timestamp
from update import scan

if __name__ == '__main__':
    current_timestamp = time()
    dist_tree = {}
    scan(dist_tree)
    print(dist_tree)
