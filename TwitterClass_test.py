import unittest

from TwitterClass import Twitter


class TestTwitter(unittest.TestCase):
    def setUp(self):
        self.twitter = Twitter()

    def test_Init(self):
        self.assertTrue(self.twitter)

    def test_addMessage(self):
        #Given
        # in setUp
        #When
        self.twitter.AddMessage('Hello 2')
        #Then
        self.assertEqual(self.twitter.tweets, ['Hello 2'])

if __name__ == '__main__':
    unittest.main()
