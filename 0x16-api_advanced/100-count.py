#!/usr/bin/python3
"""Module for task 3"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words
    in word_list in the totles of all the hot posts
    of the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
            .format(subreddit), params={"after": after},
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False)
    if sub_info.status_code != 200:
        return None

    info = sub_info.json()

    hot_l = [child.get("data").get("title")
             for child in info
             .get("data")
             .get("children")]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))
