#!/usr/bin/python3

"""
This module queries the Reddit API to retrieve the top ten hot posts
from a given subreddit.
It contains a single function, top_ten, which takes the name of a
subreddit as an argument and prints the titles of the top ten hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the top ten hot
    posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: This function does not return a value. It prints the titles of
        the top ten hot posts or prints None if the subreddit does not
        exist or there is an error.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
