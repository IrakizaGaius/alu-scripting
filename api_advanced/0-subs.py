#!/usr/bin/python3
"""
Function that queries the Reddit API to get the number of subscribers of a given subreddit.
"""

import requests
import time

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers of a subreddit from the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if the subreddit is invalid.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad status codes

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers")
            return subscribers if subscribers is not None else 0
        else:
            print("Error: Status Code {}".format(response.status_code))
            return 0
    except requests.HTTPError as e:
        if e.response.status_code == 403:
            print("Error: 403 Client Error - Request is blocked. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
            return number_of_subscribers(subreddit)  # Retry the request
        else:
            print("An error occurred: {}".format(e))
            return 0
