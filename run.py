from utils.file_manager import load_cache, load_config, save_cache
from utils.elontwitter import ElonTwitter
from utils.pushbullet import send_push
from utils.robinhood import RobinhoodAPI

if __name__ == '__main__':
    config = load_config()
    cache = load_cache()

    # Log into APIs
    rh_api = RobinhoodAPI(config['rh_username'], config['rh_password'], config['rh_mfa'])
    elontw = ElonTwitter(config['tw_key'], config['tw_secret'], config['tw_bearer'])

    # Get tweet timeline.
    timeline = elontw.get_elon_timeline(cache['last_tweet_id'])
    doge_tweets = list(filter(lambda t : elontw.is_doge_tweet(t), timeline))


    # See if there are any doge tweets.
    if len(doge_tweets) > 0:
        # Send push notifications about all new doge tweets.
        for tweet in doge_tweets:
            send_push(tweet)

        # Get buying power.
        capital = rh_api.get_buying_power()

        # Get investment restrictions.
        invest_perc = config['investment_percentage']
        invest_cap = config['investment_cap']
        invest_cap = invest_cap if invest_cap else capital

        # Calculate investment amount.
        invest_amt = round(min(invest_perc * capital, invest_cap), 2)

        # Make investment.
        rh_api.limit_purchase_doge_by_price(invest_amt)

    # Update cache for future scrapes.
    if len(timeline) > 0:
        cache['last_tweet_id'] = timeline[0]['id']

    save_cache(cache)
