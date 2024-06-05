#!/usr/bin/python3

"""
This module queries the Reddit API to retrieve the number of subscribers
for a given subreddit. It contains a single function, number_of_subscribers,
which takes the name of a subreddit as an argument and returns the number
of subscribers to that subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers to the subreddit. If the subreddit does
        not exist or there is an error, the function returns 0.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.RequestException:
        return 0
