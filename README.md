# cat-reposter
Scrape reddit for cat pictures, verify it's a cat using ML and post the picture to twitter.

## Running the bot
Make a `.env` file at the root of the directory.

Environment variables you'll need:

`TWITTER_API_KEY` \
`TWITTER_API_SECRET_KEY` \
`TWITTER_ACCESS_TOKEN` \
`TWITTER_ACCESS_TOKEN_SECRET` \
`REDDIT_CLIENT_ID` \
`REDDIT_CLIENT_SECRET` \
`REDDIT_USERNAME` \
`REDDIT_PASSWORD`


These values can be obtained by making a [Reddit app](https://www.reddit.com/prefs/apps/) and a [Twitter app](https://developer.twitter.com/en) through their respective developer portals.
### Docker
```docker build -t cat-reposter .``` \
```docker run cat-reposter```

### Python 3 on local OS
```python main.py```
