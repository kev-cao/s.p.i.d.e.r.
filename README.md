# s.p.i.d.e.r.
[![License](https://img.shields.io/badge/license-MIT-informational)](https://github.com/defCoding/s.p.i.d.e.r./blob/main/LICENSE)
[![Twitter](https://img.shields.io/badge/api-Twitter-blue?color=1da1f2)](https://developer.twitter.com/en/docs/twitter-api)
[![Pushbullet](https://img.shields.io/badge/api-Pushbullet-green?color=4ab367)](https://docs.pushbullet.com/)
[![Robinhood](https://img.shields.io/badge/api-Robinhood-green?color=00c805)](http://www.robin-stocks.com/en/latest/robinhood.html)

**Stocks Program Investing Dogecoin when Elon Retweets**

## Context
I had recently gotten into stocks a bit, and was messing around with Dogecoin for the fun of it. According to various posts I had read on the subject, it turns out that whenever Elon Musk tweets about Dogecoin, the stock price trends upwards for a bit before dropping again. I figured that it'd be fun to create a bot that would detect when Elon tweets about Dogecoin and invests some amount into the cryptocurrency.

## What does it do?
When you run the script once, it checks the latest tweets from Elon and searches for any mention of "doge" or "crypto" - if it detects such a tweet, it sends a push notification to your mobile device using the Pushbullet API detailing the contents of the tweet, and then invests a set percentage of your available buying power into Dogecoin through Robinhood. I run this script every minute using a cronjob.

## Does it work?
It works in the sense that when Elon tweets something about Dogecoin or crypto, it will automatically invest in Dogecoin. If you're asking if it works in the sense that you gain money, I can make no guarantees. I put in a lot of effort to make sure that the maximum amount of money that can be invested can be set by the user, so you likely won't go bankrupt (unless you decide to make yourself go bankrupt). As a vote of confidence, I no longer have this program running on my computer. In other words, to be more explicit, do NOT think, for even a moment, that this program will make you money. In fact, you will likely lose money. I certainly did.

## How to Setup
This program uses Pushbullet and its API to send push notifications, so you will need to set up an account on Pushbullet. Once you are there, copy down your Pushbullet access token from [account settings](https://www.pushbullet.com/#settings) (you need to keep this secret).

To be able to access the Twitter API, you will need to [create a developer account with Twitter](https://developer.twitter.com/en/apply-for-access) and create a standalone application. Twitter will provide you three tokens - an API key, API secret, and bearer token. Copy this down (and keep it secret).

Lastly, you will need an account with [Robinhood](https://robinhood.com/) - once you have set up an account, enable Two-Factor Authentication (2FA), and select `Using an Authentication App`. Robinhood will then provide you a 2FA setup key - copy this down (keep this secret too).

Once you have all the above keys copied down, you can begin setting up this program. Clone the repository to your machine and download the required `pip` libraries with

```bash
$ pip install -r requirements.txt
```

Run the setup script with the following command:

```bash
$ python setup.py
```

The script will prompt you for your Robinhood email/password and the keys you copied down earlier. For those of you more security-minded, these will be copied down in a `json` config file in the `utils/` directory without any sort of encryption, so keep this in mind.

The script will also ask you what percentage of your buying power you would like to invest each time Elon tweets about Dogecoin, and will allow you to set a fixed cap on the amount invested per instance.

That's all you need to do to get the program set up. You can run the program once with

```bash
$ python run.py
```

To have the script run at regular intervals, I recommend using cronjobs if you are on Linux. I have the following bash script to run the program:

```bash
#!/bin/bash
cd /path/to/s.p.i.d.e.r_repo/utils
if [[ -f "config.json" ]]; then
  cd ..
  python run.py
fi
```

Then, in the crontab, I have the script set to run every minute but you can change this to your liking of course ([Cron Tutorial](https://phoenixnap.com/kb/set-up-cron-job-linux)).

```bash
# S.P.I.D.E.R. Script Job
* * * * * $SCRIPT_LOCATION
```
