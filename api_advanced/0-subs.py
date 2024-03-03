#!/usr/bin/python3
"""Module for task 0"""

def number_of_subscribers(subreddit):
<<<<<<< HEAD
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

=======
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
>>>>>>> cefc989a1317e63e87278cf1ee250160dc9d75f2
