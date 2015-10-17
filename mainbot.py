# Import the twythonaccess
import twythonaccess
# import the setup file
import setup
# import the streamer
from massinvandring_streamer import MassinvandringStreamer
# import the apikeys to be able to authenticate
import apikeys


# the main function will be called when this script is called in terminal
# the bash command "python3 mainbot.py" will call this function
def main():
    # start the streamer, and detect for instances of massinvandring in all Swedish tweets
    streamer = MassinvandringStreamer(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET, apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)
    streamer.statuses.filter(track = setup.trigger_words, language = "sv")


# if called directly (as in "python3 mainbot.py"), then call main() function
if __name__ == "__main__":
    main()
