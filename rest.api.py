
from flask import Flask, request, jsonify

from model import model
from urlpredict import url_predictor

app = Flask(__name__)

@app.route('/email_analyse', methods=['POST'])
def analyze_text():
    # Get the text from the request
    data = request.get_json()
    text = data['text']
    result = model(text)
    response = {
        'input_text': text,
        'result': result
    }

    # Return the response as JSON
    return jsonify(response)


@app.route('/url_analyse', methods=['POST'])
def analyze_url():
    # Get the text from the request
    data = request.get_json()
    text = data['text']
    result = url_predictor(text)
    response = {
        'input_text': text,
        'result': result
    }

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
