import requests
from config import load_config

class ElonTwitter:
    """
    Connects to Elon Musk's Twitter account and reads his tweets.
    """

    def __init__(self, key, secret, token):
        """
        Initializes the ElonTwitter object.

        Params:
        - key (string) : Consumer API Key from Twitter.
        - secret (string) : Consumer API Secret from Twitter.
        - bearer (string) : Consumer API Bearer Token from Twitter.
        """
        self.key = key
        self.secret = secret
        self.token = token
        self.base_url = 'https://api.twitter.com/1.1/'

    def _set_headers(self, session):
        """
        Adds authorization heads to requests Session.

        Params:
        - session (Session) : requests Session object.
        """
        session.headers.update({'Authorization': f'Bearer {self.token}'})

    def _connect_to_get_endpoint(self, endpoint, params):
        """
        Accesses a GET endpoint with the provided parameters.

        Params:
        - endpoint (string) : The RESTful GET endpoint.
        - params (string) : GET parameters.

        Raises:
        - Exception : If GET request fails.
        """
        with requests.Session() as session:
            self._set_headers(session)
            response = session.get(f'{self.base_url}/{endpoint}', params=params)

        if response.status_code != 200:
            return Exception(response.status_code, response.text)

        return response.json()

    def get_elon_timeline(self, since_id=None):
        """
        Retrieves tweets from Elon's timeline.

        Params:
        - since_id (string, optional) : Limits tweets to all tweets after the tweet with this ID.

        Returns:
        - (list of obj) : List of Tweet objects.
        """
        params = {'user_id': '44196397', 'screen_name': 'elonmusk'}
        return self._connect_to_get_endpoint('/statuses/user_timeline.json', params)




if __name__ == '__main__':
    config = load_config()
    elontw = ElonTwitter(config['tw_key'], config['tw_secret'], config['tw_bearer'])
    print([tweet['text'] for tweet in elontw.get_elon_timeline()])
