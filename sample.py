from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import ast,json


#consumer key, consumer secret, access token, access secret.

ckey="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
csecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
atoken="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
asecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

class listener(StreamListener):

    def on_data(self, data):

        try:
            print(data)
            print("\n")
        except:
            raise Exception
        return(True)

    def on_error(self, status):
        
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["csk","mi",'srh',"rr","kkr",'kxip','rcb','dd'])

# api=tweepy.API(auth)
