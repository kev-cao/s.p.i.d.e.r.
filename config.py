import json

def load_config():
    """
    Loads the configuration file.

    Returns:
    - (json) - The configuration file.

    Raises:
    - FileNotFoundError: If config.json file does not exist.
    """
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Make sure to run setup.py before running this program.")
