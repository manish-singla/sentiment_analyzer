from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

### read port number for multiple testing
import sys
arguments = sys.argv
port = arguments[1]


# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_csv', methods=['POST'])
def process_csv():
    # Process entire CSV and update chart
    # Implement CSV processing and sentiment analysis
    return jsonify(chart_data)

@app.route('/process_tag', methods=['POST'])
def process_tag():
    # Process tweets with given #tag and update chart
    hashtag = request.form['hashtag']
    # Implement CSV processing and sentiment analysis for tweets with the given hashtag
    return jsonify(chart_data)

@app.route('/process_tweet', methods=['POST'])
def process_tweet():
    # Process user entered tweet and update chart
    tweet = request.form['tweet']
    # Implement sentiment analysis for the entered tweet
    # Perform sentiment analysis

    data = analyze_sentiment(tweet)
    data = jsonify(data)
    print(data)
    return data

def analyze_sentiment(tweet):
	# Determine the overall sentiment
	# Perform sentiment analysis
	sentiment_scores = sia.polarity_scores(tweet)
	data = [sentiment_scores['pos'],sentiment_scores['neg'],sentiment_scores['neu']]
	return data
		

if __name__ == '__main__':
    app.run(debug=True, port = port)



