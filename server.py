"""
This module contains the implementation of a web server for the Emotion Detection Web App.
It handles incoming HTTP requests, serves web pages, and provides API endpoints.

Author: Thiago Bottoni
Date: October 31, 2023
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    ''' This function calls the emotion_detection module and returns the results '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return f"For the given statement, the system response is \
        'anger': {response['anger']}, \
        'disgust': {response['disgust']}, \
        'fear': {response['fear']}, \
        'joy': {response['joy']} and \
        'sadness': {response['sadness']}. \
        The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    '''This renders the web page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
