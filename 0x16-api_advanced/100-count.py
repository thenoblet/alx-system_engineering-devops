#!/usr/bin/python3

"""
This module queries the Reddit API to count occurrences of specified
keywords in the titles of hot posts from a given subreddit.
It contains three functions:
1. fetch_hot_posts: Fetches the JSON response of hot posts from Reddit
for a given subreddit.
2. count_keywords_in_title: Counts occurrences of specified
keywords in a title.
3. count_words: Recursively counts occurrences of specified keywords in
the titles of all hot posts from a given subreddit.
"""

import requests
from collections import defaultdict


def fetch_hot_posts(subreddit, after=None):
    """
    Fetches the JSON response of hot posts from Reddit for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        after (str): A token indicating the next page of results
        (used for pagination).

    Returns:
        dict or None: A dictionary containing the JSON response of hot posts,
        or None if there is an error.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException:
        return None


def count_keywords_in_title(title, word_list):
    """
    Counts occurrences of specified keywords in a title.

    Args:
        title (str): The title of a Reddit post.
        word_list (list): A list of keywords to search for in the title.

    Returns:
        defaultdict: A dictionary with keyword counts in the title.
    """
    words = title.lower().split()
    keyword_counts = defaultdict(int)
    for word in word_list:
        keyword = word.lower()
        keyword_counts[keyword] += words.count(keyword)
    return keyword_counts


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively counts occurrences of specified keywords in the titles
    of all hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to search for in the titles.
        after (str): A token indicating the next page of results
        (used for pagination).
        word_count (defaultdict): A dictionary to store the counts of
        keywords (used for recursion).

    Returns:
        None: This function does not return a value. It prints the counts of
        keywords in the titles of hot posts.
    """
    if word_count is None:
        word_count = defaultdict(int)

    data = fetch_hot_posts(subreddit, after)
    if data:
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            title_word_count = count_keywords_in_title(title, word_list)
            for word, count in title_word_count.items():
                word_count[word] += count
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(
                    word_count.items(),
                    key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
            return
    else:
        return
