# hacker-news-bot 👩‍💻

An AWS Lambda function that scrapes the [Hacker News](https://news.ycombinator.com/) and posts a tweet.

## Table of contents 📕
- [Tech](#tech)
- [Workflow](#workflow)
- [Launch](#launch)
- [Deploy](#deploy)


## Tech
- [Python 3]()
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Tweepy](https://docs.tweepy.org/en/stable/)
- [requests](https://pypi.org/project/requests/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

## Workflow 
![workflow-image](/assets/workflow.png)


## Launch

Create a new virtual environment.
```
$ python3 -m venv venv
```

```
$ source venv/bin/activate
```

Install dependencies.
```
$ pip install -r requirements.txt
```

Create a new `.env` file with the structure below.
```
CONSUMER_KEY=
CONSUMER_SECRET=
ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=
```

```
$ python main.py
```


You can get keys and tokens [here](https://developer.twitter.com/en/portal/dashboard).

## Deploy

You can generate a `.zip` with all the necessary packages to upload to `AWS Lambda`.

```
$ ./deploy.sh
```