# the MassinvandringStreamer is a subclass of TwythonStreamer
from twython import TwythonStreamer
# import twythonaccess, to be able to send tweets
from . import twythonaccess
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
        if re.search(r'["\'›‹»«]massinvandring\w*["\'›‹»«]', tweet["text"]):
            return
        # if tweet is from self, return here
        if tweet["user"]["screen_name"] == twythonaccess.screen_name:
            return
        if tweet["user"]["id"] in self.replied_to_users:
            return
        # user isn't being obviously ironic or critical
        replies = ["Tänk om du varit född i Syrien. Eller i Afghanistan. Eller Irak.",
                "Du hade fått välja mellan att ta med din familj på en livsfarlig resa till ett bättre liv, eller riskera bli dödad.",
                "Du hade valt det senare, för du hade älskat din familj och dina barn.",
                "Du hade med mycket möda lyckats ta dig till Sverige. Puh, barnen lever!",
                "Så blir du bemött av dig själv, i det som du trodde var det öppna Sverige.",
                "'Jag hade turen att födas här, och jag är rädd att jag ska få det lite sämre om jag hjälper dig. Tillbaka till döden!'",
                "Du hade turen att födas i Sverige. Dela med dig av den turen."]
        for index, reply in enumerate(replies):
            replies[index] = "@" + tweet["user"]["screen_name"] + " " + reply
        #reply = "@" + tweet["user"]["screen_name"] + " Jag rekommenderar följande rapport från OECD på ämnet: http://oecd.org/migration/mig/OECD%20Migration%20Policy%20Debates%20Numero%202.pdf. Deras slutsats: massinvandring är bra. Läs!"
        # try to send the reply (not guaranteed)
        if twythonaccess.send_rant(tweets = replies, in_reply_to_status_id = tweet["id"]):
            replied_to_users.append(tweet["user"]["id"])
            


    # when an error is caught
    def on_error(self, status_code, data):
        print("STREAMING API ERROR!")
        print("Status code:")
        print(status_code)
        print("Other data:")
        print(data)
        print("END OF ERROR MESSAGE")
