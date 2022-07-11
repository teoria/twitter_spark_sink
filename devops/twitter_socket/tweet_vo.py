from dataclasses import dataclass

@dataclass
class TweetVO:
    tweet: dict

    def __str__(self):
        text = self.tweet['extended_tweet']['full_text'] if 'extended_tweet' in self.tweet.keys() \
                   else self.tweet['text']
        text = text.replace('\n', ' ').replace('\r', ' ')
        msg = [str(self.tweet['id']),
#               str(self.tweet['user']['name']),
#               str(self.tweet['user']['screen_name']),
               str(text) #,
#               str(self.tweet['user']['followers_count']),
#               str(self.tweet['lang']),
#               str(self.tweet['created_at']),
 #              str(self.tweet['timestamp_ms'])
               ]

        return '<@#$>'.join(msg) + 't_end'

ZZ