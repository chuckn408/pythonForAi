import requests
import json
import unittest
 
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions']['emotion']
    score = formatted_response['emotionPredictions']['score']
    #return {formatted_response}
    return {'emotion': emotion, 'score': score}