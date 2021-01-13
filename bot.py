import tweepy 
import datetime
import os
from time import sleep
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def liketweets():
    dt=datetime.datetime.now()
    
    
    if dt.minute%10==0:
        cur=tweepy.Cursor(api.search, q=('#MUN OR #ModelUnitedNations'),count=1,
                       result_type='recent',lang='en').items()
        if cur!=None:
            counter=0
            for tweet in cur:
                if counter==2:
                    break
                
                if tweet != None:
                    try:

                        tweet.favorite()
                        counter=counter+1

                        sleep(5)

                    except tweepy.TweepError as e:
                        print(e.reason)

                    except StopIteration:
                        break




def publictweet():
    
        tweettopublish = ('Invite MUNchkin to your #discord server top.gg/bot/767330479757197323 and join support server discord.com/invite/xrhhD8b7AH #MUN #modelunitednations')
        api.update_status(tweettopublish)

if __name__ == '__main__':
    
    while True:
        dt=datetime.datetime.now()
    
    
        if dt.hour==12 and dt.minute==0 and dt.second==0:
            publictweet()
        else:
            try:
                liketweets()
             except tweepy.TweepError as e:
                print(e.reason)


