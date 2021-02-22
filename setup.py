import json
import os

def clear_term():
    """Clears the terminal."""
    os.system('cls' if os.name =='nt' else 'clear')

if __name__ == '__main__':
    config = {}
    clear_term()

    print('Welcome to the Stocks Program for Investing Dogecoin when Elon Retweets (S.P.I.D.E.R)!')
    print('This program uses the Robinhood API, so you will need a Robinhood account to continue.\n')
    print('If you have an account, please enter your credentials below:')
    config['rh_username'] = input('Username (or Email): ')
    config['rh_password'] = input('Password: ')

    clear_term()
    print('The program uses Pushbullet as the service to send you a mobile push notification whenever Elon tweets.')
    print('To use Pushbullet, the program needs your Pushbullet Access Token. You can find instructions on how to find the token here: https://docs.pushbullet.com/v1/#http\n')
    config['pb_token'] = input('Token: ')

    clear_term()
    print('The program also needs to be able to access the Twitter API. To do so, you will need a developer account with Twitter (apply for one here: https://developer.twitter.com/en/portal/petition).\n')
    print('Once you have a developer account, create a Twitter app from the developer console and retrieve your consumer key, consumer secret, and bearer token.\n')

    config['tw_key'] = input('Consumer Key: ')
    config['tw_secret'] = input('Consumer Secret: ')
    config['tw_bearer'] = input('Bearer Token: ')

    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

    clear_term()
    print('Your configuration settings have been saved. You may now start the script.')


