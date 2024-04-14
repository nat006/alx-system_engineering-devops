#!/usr/bin/python3

"""
Module documentation: my_module

Recursively query Reddit API, return list w/ titles of all hot posts for sub
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store titles of hot posts. Defaults to empty

    Returns:
        list: Returns None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Linux:0x16 api.advanced:v1.0.0 (by u/nm01)'}
    params = {'limit': 100}  # Limit set to 100 to avoid pagination issues
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            if data['data']['after'] is not None:
                return recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
