#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#Variables that contains the user credentials to access Twitter API 
aaccess_token = "YOUR-ACCESS-TOKEN"
access_token_secret = "YOUR-SECRET-ACCESS-TOKEN"
consumer_key = "YOUR-CONSUMER-KEY"
consumer_secret = "YOUR-CONSUMER-SECRET"


#This is a basic listener that just prints received tweets to stdout.
class listener(StreamListener):
    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
    
    def on_data(self, data):
        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
        while (time.time() - self.time) < self.limit:
            try:
                self.tweet_data.append(data)
                return True
            except BaseException as e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass
 
        saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
	saveFile.write(u'[\n')
	saveFile.write(','.join(self.tweet_data))
	saveFile.write(u'\n]')
	saveFile.close()
	exit()
 
    def on_error(self, status):
        print statuses


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key , consumer_key_secret) #OAuth object
    auth.set_access_token(access_token, access_token_secret)
    keyword_list = ['modi']
    twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
    twitterStream.filter(track=keyword_list, languages=['en'])
