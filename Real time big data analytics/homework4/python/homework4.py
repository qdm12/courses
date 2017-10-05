#!/usr/bin/env python

from tweepy import StreamListener, OAuthHandler, Stream, API
from tweepy.parsers import JSONParser
import json
from time import time

accessToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
accessTokenSecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
apiKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
apiSecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

class Listener(StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time()
        self.limit = time_limit
        self.errors = 0
        self.f = open('outputSTREAM.txt', 'wb')
        super(Listener, self).__init__()
        
    def on_data(self, data):
        if (time() - self.start_time) < self.limit:
            parsed_data = json.loads(data)
            output = '@' + parsed_data['user']['screen_name'] + ': '
            try:
                output += parsed_data['retweeted_status']['text']
            except KeyError: #see truncated
                output += parsed_data['text']
            output = output.replace('\n', '') + '\n'
            output = output.encode('utf-8')
            print(output)  
            self.f.write(output)
            return True
        else:
            self.f.close()
            return False
                
    def on_error(self, status):
        print("An error occurred: "+str(status))
        self.errors += 1
        if self.errors == 10:
            return False # disconnects
        return True
            
def twitterApi(auth, terms):
    api = API(auth, parser=JSONParser())
    parsed_data = api.search(terms)
    with open("outputAPI.txt", "wb") as f:
        for i in range(len(parsed_data['statuses'])):
            output = '@' + parsed_data['statuses'][i]['user']['screen_name'] + ': ' + parsed_data['statuses'][i]['text']
            output = output.replace('\n', '') + '\n'
            output = output.encode('utf-8')
            print(output)
            f.write(output)
            
            
if __name__ == '__main__':
    mode = "stream"
    auth = OAuthHandler(apiKey, apiSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    if mode == "stream":
        stream = Stream(auth, Listener(time_limit=5))
        stream.filter(track=["hadoop", "data"]) #can become non-blocking with async=True
    else: #we use the API search
        twitterApi(auth, "hadoop data")
    print("Program finished.")