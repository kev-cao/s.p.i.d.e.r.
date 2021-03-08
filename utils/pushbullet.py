from utils.file_manager import load_config
import requests
import json

config = load_config()

def send_push(tweet):
    """
    Sends a push notification with tweet details.

    Params:
    - tweet (obj) : Tweet object to send.

    Raises:
    - ConnectionError : If push fails.
    """
    access_token = config['pb_token']
    message = {
            'type': 'note', 
            'title': 'Elon Tweet',
            'body': tweet['text']
            }

    res = requests.post('https://api.pushbullet.com/v2/pushes',
            data=json.dumps(message),
            headers={
                'Access-Token': access_token,
                'Content-Type': 'application/json'
                })
    
    if res.status_code != 200:
        raise ConnectionError(res.text)


