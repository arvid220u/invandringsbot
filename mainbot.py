# Import the twython module
from . import twythonaccess
# import the streamer
from .massinvandring_streamer import MassinvandringStreamer
# import the apikeys to be able to authenticate
from . import apikeys


# the main function will be called when this script is called in terminal
# the bash command "python3 mainbot.py" will call this function
def main():
    # start the streamer, and detect for instances of massinvandring in all Swedish tweets
    streamer = MassinvandringStreamer(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET, apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)
    streamer.statuses.filter(track = "massinvandring,massinvandringen", language = "sv")


# if called directly (as in "python3 mainbot.py"), then call main() function
if __name__ == "__main__":
    main()
