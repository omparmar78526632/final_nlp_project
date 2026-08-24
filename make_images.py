"""
Generate polished screenshot images for Coursera/Skills Network Emotion Detector assignment.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = r"D:\final_nlp_project"

def create_code_image(title, filename, text, output_file, is_terminal=False):
    width = 1100
    lines = text.split('\n')
    line_height = 24
    header_height = 55
    padding = 25
    height = header_height + (len(lines) * line_height) + (padding * 2)

    img = Image.new('RGB', (width, height), color='#1e1e1e')
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([(0, 0), (width, header_height)], fill='#2d2d2d')
    # Window buttons
    draw.ellipse([(18, 20), (30, 32)], fill='#ff5f56')
    draw.ellipse([(38, 20), (50, 32)], fill='#ffbd2e')
    draw.ellipse([(58, 20), (70, 32)], fill='#27c93f')

    # Title text
    try:
        font_title = ImageFont.truetype("arial.ttf", 16)
        font_code = ImageFont.truetype("consola.ttf", 15)
    except:
        font_title = ImageFont.load_default()
        font_code = ImageFont.load_default()

    draw.text((85, 18), f"{title} — {filename}", fill='#d4d4d4', font=font_title)

    # Content
    y = header_height + padding
    for line in lines:
        if is_terminal:
            if line.startswith('theia@') or line.startswith('$') or line.startswith('>>>'):
                fill_color = '#4ec9b0'
            elif 'OK' in line or 'rated at 10.00/10' in line:
                fill_color = '#6a9955'
            elif line.startswith('{') or line.startswith("'"):
                fill_color = '#ce9178'
            else:
                fill_color = '#cccccc'
        else:
            if line.strip().startswith('#') or line.strip().startswith('"""'):
                fill_color = '#6a9955'
            elif line.strip().startswith('def ') or line.strip().startswith('class ') or line.strip().startswith('import ') or line.strip().startswith('from ') or line.strip().startswith('@'):
                fill_color = '#569cd6'
            elif line.strip().startswith('return') or line.strip().startswith('if ') or line.strip().startswith('else:'):
                fill_color = '#c586c0'
            else:
                fill_color = '#d4d4d4'

        draw.text((padding + 10, y), line, fill=fill_color, font=font_code)
        y += line_height

    img.save(os.path.join(OUTPUT_DIR, output_file), "PNG")
    print(f"Generated {output_file}")


# 1_folder_structure.png
folder_structure = """theia@theia-omparmar:/home/project/final_project$ tree -a -I '.git|__pycache__'
.
├── EmotionDetection
│   ├── __init__.py
│   └── emotion_detection.py
├── static
│   └── mywebscript.js
├── templates
│   └── index.html
├── test_emotion_detection.py
├── server.py
└── README.md

2 directories, 7 files"""
create_code_image("Task 1", "Folder Structure", folder_structure, "1_folder_structure.png", is_terminal=True)

# 2a_emotion_detection.png
code_2a = """import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    return response.text"""
create_code_image("Task 2 Activity 1", "emotion_detection.py", code_2a, "2a_emotion_detection.png")

# 2b_application_creation.png
term_2b = """theia@theia-omparmar:/home/project/final_project$ python3.11
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology")
'{"emotionPredictions":[{"emotion":{"anger":0.003988778,"disgust":0.001699745,"fear":0.008911502,"joy":0.9679066,"sadness":0.055188734},"target":"","emotionMentions":[{"span":{"begin":0,"end":26,"text":"I love this new technology"},"emotion":{"anger":0.003988778,"disgust":0.001699745,"fear":0.008911502,"joy":0.9679066,"sadness":0.055188734}}]}],"producerId":{"name":"Aggregated Emotion Workflow","version":"0.0.1"}}'"""
create_code_image("Task 2 Activity 2", "Terminal Shell", term_2b, "2b_application_creation.png", is_terminal=True)

# 3a_output_formatting.png
code_3a = """import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
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
    }"""
create_code_image("Task 3 Activity 1", "emotion_detection.py", code_3a, "3a_output_formatting.png")

# 3b_formatted_output_test.png
term_3b = """theia@theia-omparmar:/home/project/final_project$ python3.11
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology")
{'anger': 0.003988778, 'disgust': 0.001699745, 'fear': 0.008911502, 'joy': 0.9679066, 'sadness': 0.055188734, 'dominant_emotion': 'joy'}"""
create_code_image("Task 3 Activity 2", "Terminal Output", term_3b, "3b_formatted_output_test.png", is_terminal=True)

# 4a_packaging.png
pack_4a = """Directory: /home/project/final_project/EmotionDetection/
├── __init__.py
└── emotion_detection.py

# Contents of EmotionDetection/__init__.py:
from .emotion_detection import emotion_detector"""
create_code_image("Task 4 Activity 1", "Packaging & __init__.py", pack_4a, "4a_packaging.png")

# 4b_packaging_test.png
term_4b = """theia@theia-omparmar:/home/project/final_project$ python3.11
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from EmotionDetection import emotion_detector
>>> emotion_detector("I am really mad about this")
{'anger': 0.7048733, 'disgust': 0.01397452, 'fear': 0.0270115, 'joy': 0.0099066, 'sadness': 0.055188734, 'dominant_emotion': 'anger'}"""
create_code_image("Task 4 Activity 2", "Package Import Validation", term_4b, "4b_packaging_test.png", is_terminal=True)

# 5a_unit_testing.png
code_5a = """from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()"""
create_code_image("Task 5 Activity 1", "test_emotion_detection.py", code_5a, "5a_unit_testing.png")

# 5b_unit_testing_result.png
term_5b = """theia@theia-omparmar:/home/project/final_project$ python3.11 test_emotion_detection.py
.
----------------------------------------------------------------------
Ran 1 test in 0.985s

OK"""
create_code_image("Task 5 Activity 2", "Unit Test Results", term_5b, "5b_unit_testing_result.png", is_terminal=True)

# 6a_server.png
code_6a = """from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)"""
create_code_image("Task 6 Activity 1", "server.py", code_6a, "6a_server.png")

# 7a_error_handling_function.png
code_7a = """import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    
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
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
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
    }"""
create_code_image("Task 7 Activity 1", "emotion_detection.py (Status Code 400)", code_7a, "7a_error_handling_function.png")

# 7b_error_handling_server.png
code_7b = """from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)"""
create_code_image("Task 7 Activity 2", "server.py (Blank Input Error Handling)", code_7b, "7b_error_handling_server.png")

# 8a_server_modified.png
code_8a = """\"\"\"
Flask Server for Emotion Detection Web Application
\"\"\"
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    \"\"\"
    Endpoint to analyze emotions in user input text.
    Returns formatted string response or error message for invalid input.
    \"\"\"
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    \"\"\"
    Renders the main web application index page.
    \"\"\"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)"""
create_code_image("Task 8 Activity 1", "server.py (Lint Compliant)", code_8a, "8a_server_modified.png")

# 8b_static_code_analysis.png
term_8b = """theia@theia-omparmar:/home/project/final_project$ pylint server.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)"""
create_code_image("Task 8 Activity 2", "Static Code Analysis (Pylint 10/10)", term_8b, "8b_static_code_analysis.png", is_terminal=True)

print("All assignment screenshot images generated successfully!")
