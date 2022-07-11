
import tweepy
import logging


class TweetsStreamClient(tweepy.Stream):

    def on_data(self, data):
        try:
            if self.callback:
                self.callback(data)

        except BaseException as e:
            logging.exception("Error on_data:")

