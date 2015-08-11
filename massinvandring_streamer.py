# the MassinvandringStreamer is a subclass of TwythonStreamer
from twython import TwythonStreamer

# the MassinvandringStreamer class will use the streaming api to find tweets containing the word 'massinvandring'
# This class could technically be used to reply to all kinds of tweets.
class MassinvandringStreamer(TwythonStreamer):
    # this function will be called when a tweet is received
    def on_success(self, data):
        # generate a reply
        print("should generate a reply; not implemented yet though")

    # when an error is caught
    def on_error(self, status_code, data):
        print("STREAMING API ERROR!")
        print("Status code:")
        print(status_code)
        print("Other data:")
        print(data)
        print("END OF ERROR MESSAGE")
