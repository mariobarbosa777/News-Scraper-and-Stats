from flask import Flask, request, make_response, redirect , render_template, url_for, flash , json, jsonify
from flask_bootstrap import Bootstrap
from pipeline import get_data_news

app = Flask(__name__)
bootstrap = Bootstrap(app)

response_news, response_stats = get_data_news(exportCSV = False)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.route("/")
def index():

    context={}

    return render_template("hello.html", **context)


@app.route("/api_news")
def api_news_scrapper():
    
    return jsonify(response_news)

@app.route("/api_stats")
def api_news_stats():

    return jsonify(response_stats)

    