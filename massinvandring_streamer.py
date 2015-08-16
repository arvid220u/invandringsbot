# the MassinvandringStreamer is a subclass of TwythonStreamer
from twython import TwythonStreamer
# import twythonaccess, to be able to send tweets
from . import twythonaccess
# import regex, to be able to filter out sarcastic tweets
import re

# the MassinvandringStreamer class will use the streaming api to find tweets containing the word 'massinvandring'
# This class could technically be used to reply to all kinds of tweets.
class MassinvandringStreamer(TwythonStreamer):
    # this function will be called when a tweet is received
    def on_success(self, tweet):
        # generate a reply
        # first check so massinvandring isn't in quotes
        # this is to remove tweets that aren't genuinely xenophobic
        if re.search(r'["\'›‹»«]massinvandring\w*["\'›‹»«]', tweet["text"]):
            return
        # if tweet is from self, return here
        if tweet["user"]["screen_name"] == twythonaccess.screen_name:
            return
        # user isn't being obviously ironic or critical
        # then reply with the oecd report
        reply = "@" + tweet["user"]["screen_name"] + " Jag rekommenderar följande rapport från OECD på ämnet: http://oecd.org/migration/mig/OECD%20Migration%20Policy%20Debates%20Numero%202.pdf. Deras slutsats: massinvandring är bra. Läs!"
        # try to send the reply (not guaranteed)
        twythonaccess.send_tweet(tweet = reply, in_reply_to_status_id = tweet["id"])


    # when an error is caught
    def on_error(self, status_code, data):
        print("STREAMING API ERROR!")
        print("Status code:")
        print(status_code)
        print("Other data:")
        print(data)
        print("END OF ERROR MESSAGE")
