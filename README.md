# final_nlp_project - Emotion Detection Application

An AI-based web application deployed using Flask that performs Emotion Detection on given text using the Watson NLP library.

## Project Details
- **Project Name:** final_nlp_project
- **Package Name:** EmotionDetection
- **Application:** Emotion Detector Web Application
- **Framework:** Flask & IBM Watson NLP Library

## Features
- Detects emotions: anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Packaged as a reusable Python package `EmotionDetection`.
- Unit-tested using Python's `unittest` framework.
- Deployed with a Flask web server and clean UI.
- Robust error handling for invalid and blank inputs (status code 400).
- 10/10 Pylint static code analysis compliance.

## Project Structure
```
final_nlp_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── test_emotion_detection.py
├── server.py
└── README.md
```
