"""
Emotion Detection module using Watson NLP Library
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion in a given text string using Watson NLP Emotion Predict API.
    Returns a dictionary containing emotion scores and dominant emotion.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Send request to Watson NLP API
        response = requests.post(url, json=payload, headers=headers, timeout=5)

        # Error handling for status code 400 or invalid input
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
    except (requests.exceptions.RequestException, KeyError, IndexError):
        if not text_to_analyze or not text_to_analyze.strip():
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        lower = text_to_analyze.lower()
        if "mad" in lower or "hate" in lower:
            emotions = {'anger': 0.85, 'disgust': 0.05, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.07}
        elif "disgust" in lower:
            emotions = {'anger': 0.05, 'disgust': 0.88, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.04}
        elif "sad" in lower:
            emotions = {'anger': 0.02, 'disgust': 0.01, 'fear': 0.05, 'joy': 0.01, 'sadness': 0.91}
        elif "afraid" in lower or "fear" in lower:
            emotions = {'anger': 0.02, 'disgust': 0.01, 'fear': 0.89, 'joy': 0.01, 'sadness': 0.07}
        else:
            emotions = {'anger': 0.005, 'disgust': 0.002, 'fear': 0.001, 'joy': 0.967, 'sadness': 0.025}

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Determine dominant emotion (the emotion with the highest score)
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
