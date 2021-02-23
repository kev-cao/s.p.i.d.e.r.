from utils.file_manager import load_cache, load_config, save_cache
from utils.elontwitter import ElonTwitter
from utils.pushbullet import send_push

if __name__ == '__main__':
    config = load_config()
    cache = load_cache()

    elontw = ElonTwitter(config['tw_key'], config['tw_secret'], config['tw_bearer'])
    timeline = elontw.get_elon_timeline(cache['last_tweet_id'])
    print(timeline)
    print()
    doge_tweets = filter(lambda t : elontw.is_doge_tweet(t), timeline)

    for tweet in doge_tweets:
        send_push(tweet)

    if len(timeline) > 0:
        cache['last_tweet_id'] = timeline[0]['id']
    save_cache(cache)
