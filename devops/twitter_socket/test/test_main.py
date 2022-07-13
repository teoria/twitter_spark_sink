
import pytest 
from twitter_socket.tweet_vo import TweetVO 

msg_dict = {
  "created_at": "Fri Jul 08 10:01:33 +0000 2022",
  "id": 1545347347391172600,
  "id_str": "1545347347391172608",
  "text": "RT @DrWallaceLima: Quem for votar no Lula me segue q eu sigo de volta. Esquerda segue esquerda! @Nilsonhandebol",
  "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
  "truncated": False,
  "in_reply_to_status_id": None,
  "in_reply_to_status_id_str": None,
  "in_reply_to_user_id": None,
  "in_reply_to_user_id_str": None,
  "in_reply_to_screen_name": None,
  "user": {
    "id": 1523457713543561200,
    "id_str": "1523457713543561217",
    "name": "Marcos",
    "screen_name": "MarcosOlufon",
    "location": None,
    "url": None,
    "description": "Esquerda segue esquerda\nLula Presidente\n❤️1️⃣3️⃣❤️\n\n#lulanoprimeiroturno",
    "translator_type": "none",
    "protected": False,
    "verified": False,
    "followers_count": 7493,
    "friends_count": 7769,
    "listed_count": 1,
    "favourites_count": 13049,
    "statuses_count": 9636,
    "created_at": "Mon May 09 00:20:17 +0000 2022",
    "utc_offset": None,
    "time_zone": None,
    "geo_enabled": False,
    "lang": None,
    "contributors_enabled": False,
    "is_translator": False,
    "profile_background_color": "F5F8FA",
    "profile_background_image_url": "",
    "profile_background_image_url_https": "",
    "profile_background_tile": False,
    "profile_link_color": "1DA1F2",
    "profile_sidebar_border_color": "C0DEED",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": True,
    "profile_image_url": "http://pbs.twimg.com/profile_images/1523458047712145408/PK_lvcnS_normal.jpg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1523458047712145408/PK_lvcnS_normal.jpg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1523457713543561217/1652056560",
    "default_profile": True,
    "default_profile_image": False,
    "following": None,
    "follow_request_sent": None,
    "notifications": None,
    "withheld_in_countries": []
  },
  "geo": None,
  "coordinates": None,
  "place": None,
  "contributors": None,
  "retweeted_status": {
    "created_at": "Fri Jul 08 00:49:07 +0000 2022",
    "id": 1545208324970483700,
    "id_str": "1545208324970483712",
    "text": "Quem for votar no Lula me segue q eu sigo de volta. Esquerda segue esquerda! @Nilsonhandebol",
    "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
    "truncated": False,
    "in_reply_to_status_id": None,
    "in_reply_to_status_id_str": None,
    "in_reply_to_user_id": None,
    "in_reply_to_user_id_str": None,
    "in_reply_to_screen_name": None,
    "user": {
      "id": 1435414373061759000,
      "id_str": "1435414373061758981",
      "name": "Dr. Wallace Lima ⚖",
      "screen_name": "DrWallaceLima",
      "location": "Coronel Fabriciano, Brasil",
      "url": None,
      "description": "Advogado, Visionário.",
      "translator_type": "none",
      "protected": False,
      "verified": False,
      "followers_count": 297,
      "friends_count": 1063,
      "listed_count": 0,
      "favourites_count": 428,
      "statuses_count": 397,
      "created_at": "Wed Sep 08 01:27:29 +0000 2021",
      "utc_offset": None,
      "time_zone": None,
      "geo_enabled": True,
      "lang": None,
      "contributors_enabled": False,
      "is_translator": False,
      "profile_background_color": "F5F8FA",
      "profile_background_image_url": "",
      "profile_background_image_url_https": "",
      "profile_background_tile": False,
      "profile_link_color": "1DA1F2",
      "profile_sidebar_border_color": "C0DEED",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": True,
      "profile_image_url": "http://pbs.twimg.com/profile_images/1468372745029406727/k3htCZcS_normal.jpg",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/1468372745029406727/k3htCZcS_normal.jpg",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/1435414373061758981/1654806650",
      "default_profile": True,
      "default_profile_image": False,
      "following": None,
      "follow_request_sent": None,
      "notifications": None,
      "withheld_in_countries": []
    },
    "geo": None,
    "coordinates": None,
    "place": None,
    "contributors": None,
    "is_quote_status": False,
    "quote_count": 0,
    "reply_count": 18,
    "retweet_count": 13,
    "favorite_count": 95,
    "entities": {
      "hashtags": [],
      "urls": [],
      "user_mentions": [
        {
          "screen_name": "Nilsonhandebol",
          "name": "N.H",
          "id": 179685756,
          "id_str": "179685756",
          "indices": [
            77,
            92
          ]
        }
      ],
      "symbols": []
    },
    "favorited": False,
    "retweeted": False,
    "filter_level": "low",
    "lang": "pt"
  },
  "is_quote_status": False,
  "quote_count": 0,
  "reply_count": 0,
  "retweet_count": 0,
  "favorite_count": 0,
  "entities": {
    "hashtags": [],
    "urls": [],
    "user_mentions": [
      {
        "screen_name": "DrWallaceLima",
        "name": "Dr. Wallace Lima ⚖",
        "id": 1435414373061759000,
        "id_str": "1435414373061758981",
        "indices": [
          3,
          17
        ]
      },
      {
        "screen_name": "Nilsonhandebol",
        "name": "N.H",
        "id": 179685756,
        "id_str": "179685756",
        "indices": [
          96,
          111
        ]
      }
    ],
    "symbols": []
  },
  "favorited": False,
  "retweeted": False,
  "filter_level": "low",
  "lang": "pt",
  "timestamp_ms": "1657274493440"
}

expected_result = '1545347347391172600<@#$>Marcos<@#$>MarcosOlufon<@#$>RT @DrWallaceLima: Quem for votar no Lula me segue q eu sigo de volta. Esquerda segue esquerda! @Nilsonhandebol<@#$>7493<@#$>pt<@#$>Fri Jul 08 10:01:33 +0000 2022<@#$>1657274493440<@#$>test<EOT>'

msg_dict['tag'] = 'test'

def test_TweetVO():
    tweet_text = str(TweetVO(msg_dict))
    assert tweet_text == expected_result

def test_raises_exception_on_empty_arguments():
    with pytest.raises(KeyError):
        tweet_text = str(TweetVO({}))
 