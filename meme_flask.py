#!/bin/env python

from flask import Flask, render_template
import requests
import json
def get_meme():
    #Uncomment these two lines and comment out the other url line if you want to use a specific meme subreddt
    #sr = "/wholesomememes"
    url = "https://meme-api.com/gimme"# + sr
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    full_meme_large = response["preview"]
    subreddit = response["subreddit"]
    link = response["postLink"]
    return meme_large, subreddit, link, full_meme_large

app = Flask(__name__)
@app.route("/")
def index():
    meme_pic,subreddit, link, full_meme_large = get_meme()
    url = "https://meme-api.herokuapp.com/gimme"
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, url=url, link=link, full_meme_large=full_meme_large)

app.run(host="0.0.0.0", port=5000, debug=True)
