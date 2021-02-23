from utils.file_manager import load_cache, load_config, save_cache
from utils.elontwitter import ElonTwitter
from utils.pushbullet import send_push
from utils.robinhood import RobinhoodAPI

if __name__ == '__main__':
    config = load_config()
    cache = load_cache()

    rh_api = RobinhoodAPI(config['rh_username'], config['rh_password'], config['rh_mfa'])

    elontw = ElonTwitter(config['tw_key'], config['tw_secret'], config['tw_bearer'])
    timeline = elontw.get_elon_timeline(cache['last_tweet_id'])
    doge_tweets = list(filter(lambda t : elontw.is_doge_tweet(t), timeline))

    for tweet in doge_tweets:
        send_push(tweet)

    if len(doge_tweets) > 0:
        rh_api.limit_purchase_doge_by_price(1)
        print('Purchased.')

    if len(timeline) > 0:
        cache['last_tweet_id'] = timeline[0]['id']
    save_cache(cache)
