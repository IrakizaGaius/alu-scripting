#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to get number of Subscribers
    """
    
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "I am Learning python"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        RESPONSE.raise_for_status()  # Raise an exception for bad status codes

        data = RESPONSE.json()
        subscribers = data.get("data", {}).get("subscribers")
        return subscribers if subscribers is not None else 0

    except requests.RequestException as e:
        print("An error occurred: {}".format(e))
        return 0

