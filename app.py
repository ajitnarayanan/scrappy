from flask import Flask
app = Flask(__name__)



@app.route("/scraper/scrape") 
def home():
    return "Hello, Flask!"
