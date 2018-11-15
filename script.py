import tweepy
from datetime import datetime, timedelta

test = False
verbose = True
delete_tweets = True
delete_favs = False
days_to_keep = 30

tweets_to_save = []
favs_to_save = []

# auth shit
consumer_key = '' 
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


days_you_want_to_keep = datetime.utcnow() - timedelta(days=days_to_keep) #replace days_to_keep for a integer

if delete_tweets:
    timeline = tweepy.Cursor(api.user_timeline).items()
    deletion_count = 0
    ignored_count = 0
    #This depends on how many tweets do you have, may take a while, run in a vpn 24/7
    for tweet in timeline:
        if tweet.id not in tweets_to_save and tweet.created_at < cutoff_date:
            if verbose:
                print(f"Deleting {tweet.id}: [{tweet.created_at}] {tweet.text}")
            if not test:
                api.destroy_status(tweet.id)
            deletion_count += 1
        else:
            ignored_count += 1

    print(f"Deleted {deletion_count} tweets, ignored {ignored_count}")
else:
    print("Not deleting tweets")
