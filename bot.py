import tweepy 
import datetime
import os
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def publictweet():
    dt=datetime.datetime.now()
    
    
    if dt.hours==13 and dt.minutes==0 and dt.seconds==0:
        tweettopublish = ('Invite MUNchkin to your #discord server top.gg/bot/767330479757197323 and join support server discord.com/invite/xrhhD8b7AH #MUN #modelunitednations')
        api.update_status(tweettopublish)
publictweet()
