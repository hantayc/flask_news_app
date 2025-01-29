from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

# Createa Flask app
app = Flask(__name__)


# Homepage  - Route
# Home / About / Contact / Pricing
@app.route("/")
def index():
    # Get the news from the API
    query = request.args.get("query", "latest")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"  # "latest" is the default query
    response = requests.get(url)  # retrieve the data
    news_data = response.json()  # convert the data to json

    articles = news_data.get("articles", [])

    filtered_articles = [
        article
        for article in articles
        if "Yahoo" not in article["source"]["name"]
        and "removed" not in article["title"].lower()
    ]

    return render_template("index.html", articles=filtered_articles, query=query)


# Define the route for the home page
if __name__ == "__main__":
    app.run(
        debug=True
    )  # Run the app in debug mode so we don't have to restart the terminal
