from flask import Flask
app = Flask(__name__)



@app.route("/scraper/scrape",methods=['GET']) 
def home():
    return "Hello, Flask!"



@app.route('/scraper/healthCheck', methods=['GET'])
def health_check():
    return "Hello, Welcome"




if __name__ == "__main__":
    app.run()