#!/usr/bin/python3

"""
Module documentation: my_module

Recursively query Reddit API, parse title of hot posts, print sorted count
"""

import requests
import re
from collections import Counter


def count_words(subreddit, word_list, counts=None):
    """
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences of.
        counts (Counter): To store the counts of keywords. Defaults to None

    Returns:
        None
    """
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Linux:0x16 api.advanced:v1.0.0 (by u/nm01)'}
    params = {'limit': 100}  # Limit set to 100 to avoid pagination issues
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if re.search(rf'\b{word.lower()}\b', title):
                        counts[word.lower()] += 1
            if data['data']['after'] is not None:
                return count_words(subreddit, word_list, counts=counts)
            else:
                for word, count in sorted(counts.items(),
                                        key=lambda x: (-x[1], x[0])):
                    print(f"{word}: {count}")
        else:
            print(None)
    except Exception as e:
        print(f"An error occurred: {e}")
        print(None)
