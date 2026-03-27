import unittest
from utils import detect_emotion

class TestEmotion(unittest.TestCase):
    def test_positive_text(self):
        result = detect_emotion("I am very happy today!")
        self.assertIn('joy', result)

    def test_negative_text(self):
        result = detect_emotion("I am very sad today.")
        self.assertIn('sadness', result)

if __name__ == '__main__':
    unittest.main()
