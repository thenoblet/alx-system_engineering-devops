#!/usr/bin/python3

"""
This module queries the Reddit API to recursively retrieve all hot
post titles from a given subreddit.
It contains a single function, recurse, which takes the name of a
subreddit as an argument and returns a list of titles of all hot posts.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all
    hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot posts
        (used for recursion).
        after (str): A token indicating the next page of result
        (used for pagination).

    Returns:
        list: A list of titles of all hot posts in the subreddit.
        If the subreddit does not exist or there is an error,
        the function returns None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom'}

    # Limit to 100 posts per request to reduce the number of API calls
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                url, headers=headers,
                params=params,
                allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
