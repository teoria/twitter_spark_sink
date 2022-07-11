import json
import os
import socket

from twitter_client import TweetsStreamClient
from tweet_vo import TweetVO

ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
param = os.getenv("TWITTER_PARAM").split(',')


def on_data_cb(msg):
    msg_dict = json.loads(msg)
    tweet_text = str(TweetVO(msg_dict))
    print(tweet_text.encode('utf-8'))
    conex.send(tweet_text.encode('utf-8'))

   # conex.send(str(tweet_text + "t_end").encode('utf-8'))


if __name__ == '__main__':
    conex = None
    tcp = socket.socket()
    host = "0.0.0.0"
    port = 5555
    try:
        tcp.bind((host, port))
        tcp.listen(3)
        print(f'socket escutando a porta {port}')
        conex, socket_client = tcp.accept()
        print("Received request from: " + str(socket_client))
        print(conex)
        twitter_client = TweetsStreamClient(CONSUMER_KEY,
                                            CONSUMER_SECRET,
                                            ACCESS_KEY,
                                            ACCESS_SECRET
        )
        twitter_client.callback = on_data_cb
        twitter_client.filter(track=param)
    except Exception as e:
        print(e)
    finally:
        if conex:
            conex.close()
        tcp.close()
        print('desligando')