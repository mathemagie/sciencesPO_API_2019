# Import packages and config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from config import consumer_key, consumer_secret, access_token, access_token_secret
import datetime
import csv
import requests


# Takes tweets and a designated csv file and writes them to it.

def change_color(color): 
  r = requests.get("https://changecolor-candle.glitch.me/" + color)



class StdOutListener(StreamListener):

    def on_status(self, status):
        print(status.text)
        change_color('rouge')
        # Filtering English language tweets from users with more than 500 followers
        if (status.lang == "en") & (status.user.followers_count >= 500):
            # Creating this formatting so when exported to csv the tweet stays on one line
            tweet_text = "'" + status.text.replace('\n', ' ') + "'"
            print (tweet_text)
            csvw.writerow([status.id,
                           status.user.screen_name,
                           # created_at is a datetime object, converting to just grab the month/day/year
                           status.created_at.strftime('%m/%d/%y'),
                           status.user.followers_count,
                           tweet_text])
            return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filter based on listed items
    csvw = csv.writer(open("blank.csv", "a"))
    csvw.writerow(['twitter_id', 'name', 'created_at',
                   'followers_count', 'text'])
    stream.filter(track=['sciencespo_API'])