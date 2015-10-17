# invandringsbot
When people post ignorant tweets about immigration, this bot replies with a rant about the moral responsibility we all have to welcome refugees. All in Swedish.

# How it works

Whenever anyone tweets a tweet containing a certain trigger word or phrase, invandringsbot will reply with a rant.

In this specific, original implementation of invandringsbot, the trigger word is "massinvandring" (Swedish for "mass immigration") and the rant is about the moral responsibility we have to welcome refugees (also in Swedish). However, the trigger word can be anything, as can the rant be.

# Translate into your language!

It's not only Swedes who are in need of a rant about our moral responsibilities. Make the world a better place by translating invandringsbot!

It's simple to do.

1. Clone this repository.
2. Rename the `apikeys_template.py` file to `apikeys.py`, and add your Twitter API keys as obtained from apps.twitter.com.
3. Open the `setup.py` file. Fill in your trigger word, rant, and the Twitter handle of the bot.
4. Finished setup! Now, start invandringsbot by calling `python3 mainbot.py`, when in the correct directory in your terminal.

# Dependencies

Using python 3. Has not been tested on python 2, but should work with minor optimizations.

- [Twython](https://github.com/ryanmcgrath/twython). Used for all contact with the Twitter API.
