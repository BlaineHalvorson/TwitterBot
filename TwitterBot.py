import random
import tweepy
from setup.py import *

def troll(text):
    num = random.randint(0,1)
    string = []
    for i in text:
        num = random.randint(0,1)
        if num:
            string.append(i.upper())
        else:
            string.append(i.lower())
    return "".join(string)

atSign = ["@"]

tweets = api.user_timeline(screen_name="Username Here", count=100)
for tweet in tweets:
    if tweet.text[0:2] != "RT":
        for i in atSign:
            tweet.text = tweet.text.replace(i, "")
            api.update_with_media("mocking-spongebob.jpg", "@(Username Here) {}".format(troll(tweet.text)), tweet.id)
