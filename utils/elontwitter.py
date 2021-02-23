import requests

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
        - since_id (int | string, optional) : Limits tweets to all tweets after the tweet with this ID.

        Returns:
        - (list of obj) : List of Tweet objects.
        """
        params = {'user_id': '999498208492638208', 'screen_name': 'defCoding', 'since_id': since_id}
        return self._connect_to_get_endpoint('/statuses/user_timeline.json', params)

    def is_doge_tweet(self, tweet):
        """
        Determines if a tweet references doge.

        Params:
        - tweet (obj) : Tweet object to parse.

        Returns:
        - (bool) : True/False if tweet references doge.
        """
        text = tweet['text'].lower()
        return 'doge' in text or 'crypto' in text
