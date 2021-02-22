import json
import os

def load_json_file(filename):
    """
    Loads a json file.

    Params:
    - filename (string) : The name of the file to load. Must include file extension.

    Returns:
    - (json) : The json file.

    Raises:
    - IOError : If the file does not exist.
    """
    try:
        with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
            return json.load(f)
    except IOError:
        raise IOError(f'Could not find {filename}. Make sure to run setup.py before running this program.')

def save_json_file(filename, data):
    """
    Saves data to the provided json filename.

    Params:
    - filename (string) : The name of the file to save to. Must include file extension.
    - data (dict) : The data to save to the file.
    """
    with open(os.path.join(os.path.dirname(__file__), filename), 'w') as f:
        json.dump(data, f, indent=4)

def load_config():
    """
    Loads the configuration file.

    Returns:
    - (json) : The configuration file.
    """
    return load_json_file('config.json')

def save_config(config):
    """
    Saves the given configuration to the config.json file.

    Params:
    - config (dict) : The config to save.
    """
    save_json_file('config.json', config)

def load_cache():
    """
    Loads the cache file.

    Returns:
    - (json) : The cache file.
    """
    return load_json_file('cache.json')

def save_cache(cache):
    """
    Saves the given cache to the cache.json file.

    Params:
    - cache (dict) : The cache to save.
    """
    save_json_file('cache.json', cache)
