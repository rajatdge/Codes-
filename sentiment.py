import tweepy
from textblob import TextBlob

consumer_key= '97ivQ10cr6Etb98Fg0dtIhZG6'
consumer_secret= 'vZpK4AIR674HuDh8Jhd4EnN3WsWSjUJAoDS7kiSYPBXgfmUxDM'

access_token= '2479063608-kQSZmkteG7QFk8gRATTp3rX62j7W7t7yTG0nZgj'
access_token_secret= 'pBjDzptVliPqB6aFU3gMIKb7CydgnARBAnpr0V7rAcank'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")