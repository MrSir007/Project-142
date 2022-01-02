import csv
from content_filtering import get_recommendation
from demographic_filtering import output
from main import liked_articles, unliked_articles, unwatched_articles
from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/demographic-dictionary")
def get_article () :
  return jsonify({
    "data": list(output)
  })

@app.route("/content-dictionary")
def get_article () :
  return jsonify({
    "data": list(get_recommendation(output))
  })
