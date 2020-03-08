# parse cache data structure
import json

def load_cache(filename):
    # return as a json object
    with open(filename) as f:
        return json.load(f)

def save_cache(filename, data):
    with open(filename,'w') as f:
        return json.dump(data, f)

def get_total_size(data):
    _size = 0
    for k, v in data.items():
        if type(v) is int:
            _size += v
        elif v == {}:
            _size += get_total_size(v)
        else:
            _size += 4096
    return _size 
