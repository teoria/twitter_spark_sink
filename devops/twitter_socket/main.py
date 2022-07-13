import json
import os
import socket

from twitter_client import TweetsStreamClient
from tweet_vo import TweetVO

ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
param = os.getenv("TWITTER_PARAM")


def on_data_cb(msg):
    msg_dict = json.loads(msg)
    msg_dict['tag'] = param
    tweet_text = str(TweetVO(msg_dict))
    try:
        conex.send(tweet_text.encode('utf-8'))
        print(tweet_text)
    except:
        pass


if __name__ == '__main__':
    conex = None
    tcp = socket.socket()
    host = "0.0.0.0"
    port = 5556
    try:
        tcp.bind((host, port))
        print('socket is ready') 
        tcp.listen(3)
        print('socket is listening') 
        conex, socket_client = tcp.accept()
        print("Received request from: " + str(socket_client))  

        twitter_client = TweetsStreamClient(CONSUMER_KEY,
                                            CONSUMER_SECRET,
                                            ACCESS_KEY,
                                            ACCESS_SECRET
        )
        twitter_client.callback = on_data_cb
        twitter_client.filter(track=param.split(','))
    except Exception as e:
        print(e)
    finally:
        if conex:
            conex.close()
        tcp.close()
        print('desligando')
