import os
import tweepy

from typing import List
from dotenv import load_dotenv

load_dotenv()

TWEET_CHAR_LIMIT = 280


def merge_strings_within_chars_limit(strs: List[str], limit=TWEET_CHAR_LIMIT) -> List[str]:
    result = [""]
    total_len = 0
    for s in strs:
        s_len = len(s)
        if total_len + s_len + 1 <= limit:
            total_len += (s_len + 1)
        else:
            total_len = s_len + 1
            result.append("")
        # platform independent line breaker
        result[len(result) - 1] += (s + os.linesep)
    return result


class TwitterClient:
    def __init__(self) -> None:
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        self.client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                                    access_token=access_token, access_token_secret=access_token_secret)

    def post_sequentially(self, texts: List[str]) -> None:
        reply_to = None
        for text in texts:
            resp = self.client.create_tweet(
                text=text, in_reply_to_tweet_id=reply_to)
            if len(resp.errors) == 0:
                reply_to = resp.data["id"]
