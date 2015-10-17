# the MassinvandringStreamer is a subclass of TwythonStreamer
from twython import TwythonStreamer
# import twythonaccess, to be able to send tweets
import twythonaccess
# import the setup file with the trigger word and rant
import setup
# import regex, to be able to filter out sarcastic tweets
import re

# the MassinvandringStreamer class will use the streaming api to find tweets containing the word 'massinvandring'
# This class could technically be used to reply to all kinds of tweets.
class MassinvandringStreamer(TwythonStreamer):

    # only reply to one user once
    replied_to_users = []

    # this function will be called when a tweet is received
    def on_success(self, tweet):
        # generate a reply
        # first check so massinvandring isn't in quotes
        # this is to remove tweets that aren't genuinely xenophobic
        if re.search(r'["\'›‹»«]' + setup.trigger_word + r'\w*["\'›‹»«]', tweet["text"]):
            return
        # if tweet is from self, return here
        if tweet["user"]["screen_name"] == setup.screen_name:
            return
        if tweet["user"]["id"] in self.replied_to_users:
            return
        # user isn't being obviously ironic or critical
        replies = setup.rant
        for index, reply in enumerate(replies):
            replies[index] = "@" + tweet["user"]["screen_name"] + " " + reply
        #reply = "@" + tweet["user"]["screen_name"] + " Jag rekommenderar följande rapport från OECD på ämnet: http://oecd.org/migration/mig/OECD%20Migration%20Policy%20Debates%20Numero%202.pdf. Deras slutsats: massinvandring är bra. Läs!"
        # try to send the reply (not guaranteed)
        if twythonaccess.send_rant(tweets = replies, in_reply_to_status_id = tweet["id"]):
            self.replied_to_users.append(tweet["user"]["id"])
            


    # when an error is caught
    def on_error(self, status_code, data):
        print("STREAMING API ERROR!")
        print("Status code:")
        print(status_code)
        print("Other data:")
        print(data)
        print("END OF ERROR MESSAGE")
