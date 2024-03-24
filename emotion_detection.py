#import docstring
import json
#import unittest
import requests
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    #myobj = { "raw_document": { "text": "Testing this application for error handling" } }
    response = requests.post(url, json = myobj, headers=header)
    print(response.status_code)
    formatted_response = json.loads(response)
    emotion = formatted_response['emotionPredictions']['emotion']
    score = formatted_response['emotionPredictions']['score']
    #return {formatted_response}
    return {emotion, score}