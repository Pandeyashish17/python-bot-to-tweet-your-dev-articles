#importing stuffs
import tweepy
import requests

# Replace these with your own API keys and tokens
#To see how to get keys, i will upload a video , so dont forget to check description and i will also pin in the comment
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate the bot
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#function to get articles
def get_articles():
    username = "ashishpandey"
    #change the username from yours
    url = f"https://dev.to/api/articles?username={username}"
    response = requests.get(url)
    return response.json()

#function to tweet articles
def tweet_articles(articles):
    # Tweet each article
    for article in articles:
        title = article["title"]
        link = article["url"]
        tweet_text = f"{title}\n{link}"
        api.update_status(tweet_text)


# Get the list of articles
articles = get_articles()

# Tweet all articles
tweet_articles(articles)

