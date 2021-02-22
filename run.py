from utils.file_manager import load_cache, load_config, save_cache
from utils.elontwitter import ElonTwitter

if __name__ == '__main__':
    config = load_config()
    cache = load_cache()

    elontw = ElonTwitter(config['tw_key'], config['tw_secret'], config['tw_bearer'])
    timeline = elontw.get_elon_timeline(cache['last_tweet_id'])
    print([tweet['text'] for tweet in timeline])
    cache['last_tweet_id'] = timeline[0]['id']
    save_cache(cache)
