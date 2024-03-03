#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    """'
    Function to get number of Subscribers 
    """
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'PostmanRuntime/7.35.0'}  # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0