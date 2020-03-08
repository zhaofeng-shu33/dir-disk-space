# parse cache data structure
import json

def get_cache(filename):
    # return as a json object
    with open(filename) as f:
        return json.load(f)

def save_cache(filename):
    with open(filename,'w') as f:
        return json.dump(f)

