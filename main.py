from os import environ
from flask import Flask
from requests import get
from time import time

app = Flask(__name__)

news = {}
timestamp = time()

@app.route("/")
def get_news():
    global news
    global timestamp
    if (not bool(news)) or (time() - timestamp > 86400):
        url_api = environ.get("URL_PUBLIC_NEWS_API")
        resp = get(url=url_api).json()
        news = resp['articles']
        timestamp = time()

    return { "news" : news }

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(environ.get("PORT", 8080)))