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
        self.twitter.AddMessage('Hello')
        #Then
        self.assertEqual(self.twitter.tweets, ['Hello'])

if __name__ == '__main__':
    unittest.main()
