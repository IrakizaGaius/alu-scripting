import requests
import time

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad status codes

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers")
            return subscribers if subscribers is not None else 0
        else:
            print(f"Error: Status Code {response.status_code}")
            return 0
    except requests.HTTPError as e:
        if e.response.status_code == 403:
            print("Error: 403 Client Error - Request is blocked. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
            return number_of_subscribers(subreddit)  # Retry the request
        else:
            print("An error occurred: {}".format(e)
            return 0
