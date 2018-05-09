from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import ast,json


#consumer key, consumer secret, access token, access secret.
ckey="p2UP9MRYjgfpBBYCnqiHsZ2T8"
csecret="DHajvOpEkVS5td9aBppeDcKcm6auvcKgMhyaVQ0Ks556t1QOi7"
atoken="2963944907-ilY9wfwV3LYmJmOuaIQGhrpoAK21JVRvNg1Yvap"
asecret="wFSJPAgw0B04hHhKnk9dSbYdvODxU8b5qZOBoI4beAvZt"

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
twitterStream.filter(track=["#csk","#mi",'#srh',"#rr","#kkr",'#kxip','#rcb','#dd'])

# api=tweepy.API(auth)