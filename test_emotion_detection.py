"""
Unit tests for Emotion Detection application
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test suite for testing emotion detector function
    """
    def test_joy(self):
        """Test for joy detection"""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Test for anger detection"""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Test for disgust detection"""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Test for sadness detection"""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Test for fear detection"""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
