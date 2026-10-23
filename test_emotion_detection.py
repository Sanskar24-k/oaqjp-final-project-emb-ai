import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Joy test
        res_joy = emotion_detector("I am glad this happened")
        self.assertEqual(res_joy['dominant_emotion'], 'joy')
        
        # Anger test
        res_anger = emotion_detector("I am really mad about this")
        self.assertEqual(res_anger['dominant_emotion'], 'anger')
        
        # Disgust test
        res_disgust = emotion_detector("I feel disgusted just thinking about this")
        self.assertEqual(res_disgust['dominant_emotion'], 'disgust')
        
        # Sadness test
        res_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(res_sadness['dominant_emotion'], 'sadness')
        
        # Fear test
        res_fear = emotion_detector("I am really afraid this will happen")
        self.assertEqual(res_fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
