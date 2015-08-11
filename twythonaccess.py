# This module provides the api twython object, which is used to access the api

# import time, to enable the sleep function
import time

# Import twython
from twython import Twython

# import the api keys
import apikeys




# The api variable is the way to access the api
def authorize():
    # Increment number of requests made
    global requests_since_last_sleep
    requests_since_last_sleep += 1
    # authorize
    return Twython(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET, apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)

# the screen name for self
screen_name = "invandringgarna"

# this method sends a tweet, by first checking with me
def send_tweet(tweet, in_reply_to_status_id=0):
    global screen_name
    
    # send tweet
    check_if_requests_are_maximum(13)
    # maybe send it in reply to another tweet
    if in_reply_to_status_id == 0:
        # standalone tweet
        authorize().update_status(status=tweet)
    else:
        # tweet is a reply
        authorize().update_status(status=tweet, in_reply_to_status_id=in_reply_to_status_id)
    print("sent tweet: " + tweet)


# Store number of requests, so that they won't exceed the rate limit
requests_since_last_sleep = 0
# This method is called every time a request is to be made
# If the requests variable is over limit, then it sleeps for 16 minutes
# if the requests variable isn't over limit, then do nothing
def sleep_if_requests_are_maximum(limit):
    global requests_since_last_sleep
    print("Requests since last sleep: " + str(requests_since_last_sleep))
    if requests_since_last_sleep >= limit:
        print("will sleep")
        time.sleep(16*60)
        print("has slept")
        # reset requests
        requests_since_last_sleep = 0
