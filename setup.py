import json
import os
from utils.file_manager import save_config, save_cache
from utils.robinhood import RobinhoodAPI

def clear_term():
    """Clears the terminal."""
    os.system('cls' if os.name =='nt' else 'clear')

if __name__ == '__main__':
    # Config is saved to file for persistent storage.
    config = {}
    clear_term()

    # Get information needed for config file.
    print('Welcome to the Stocks Program for Investing Dogecoin when Elon Retweets (S.P.I.D.E.R)!')
    print('This program uses the Robinhood API, so you will need a Robinhood account to continue.\n')
    print('If you have an account, please enter your credentials below:')
    config['rh_username'] = input('Username (or Email): ')
    config['rh_password'] = input('Password: ')

    print('\nYou will need to enable two-factor authentication on your Robinhood account, and set your authentication method to "other".')
    print('You will be given a MFA key. Please enter it here.')
    config['rh_mfa'] = input('MFA Key: ')

    print('We will attempt to connect to your Robinhood account now. Please enter your authentication code when prompted.')
    RobinhoodAPI(config['rh_username'], config['rh_password'], config['rh_mfa'])
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

    clear_term()
    print('Time to set limits on the investment amounts.')
    print('What percentage of your buying power would you like to use per investment?')
    
    percentage = float(input('Enter a percentage (0 - 100): '))
    if not (0 <= percentage <= 100):
        raise Exception('Not a valid percentage.')

    config['investment_percentage'] = percentage / 100

    print('What is the absolute cap you would like to set per investment in USD?')
    cap = input('Enter a cap (leave empty for no hard cap): $')

    if cap == '':
        cap = None
    else:
        cap = float(cap)
        if cap <= 0:
            raise Exception('The cap must be a positive nonzero value.')

    config['investment_cap'] = cap

    # Setting up cache for determining latest processed tweet.
    cache = {}
    cache['last_tweet_id'] = None

    save_cache(cache)
    save_config(config)

    clear_term()
    print('Your configuration settings have been saved. You may now start the script.')
