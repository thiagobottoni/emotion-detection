"""
This is a Python module for extracting emotions from comments.

Author: Thiago Bottoni
Date: October 31, 2023
"""
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        all_scores = formatted_response['emotionPredictions'][0]['emotion']
        key_emotion = max(all_scores, key=all_scores.get)
        formatted_output = {
                'anger': all_scores['anger'],
                'disgust': all_scores['disgust'],
                'fear': all_scores['fear'],
                'joy': all_scores['joy'],
                'sadness': all_scores['sadness'],
                'dominant_emotion': key_emotion
            }
    else:
        formatted_output = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    return formatted_output
