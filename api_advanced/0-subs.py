#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Gaius2324'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad status codes

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers")
            return subscribers if subscribers is not None else 0
        else:
            print("Error: Status Code", response.status_code)
            return 0
    except requests.RequestException as e:
        print("An error occurred:", e)
        return 0
