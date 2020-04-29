import random
import tweepy

auth = tweepy.OAuthHandler("bbhTsieJyckbAksSFqD4JC31b","rSz1dQGuvCSJ5sws08JjWm9KuQLvlMKMch4ycSxveJHr0hWq9X")
auth.set_access_token("1249884242642960384-eyNRtVvApEXqG6J6Pbi1YWYucnCd0c","bqCOTtTQ5VCHyC0n2BMt4ay8ckWA9ElcUwvpTbqq5IRQT")
api = tweepy.API(auth)

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

tweets = api.user_timeline(screen_name="Hotpocketlxrd", count=100)
for tweet in tweets:
    if tweet.text[0:2] != "RT":
        for i in atSign:
            tweet.text = tweet.text.replace(i, "")
            api.update_with_media("mocking-spongebob.jpg", "@Hotpocketlxrd {}".format(troll(tweet.text)), tweet.id)
