import unittest

from TwitterClass import Twitter


class TestTwitter(unittest.TestCase):

    def test_Init(self):
        twitter = Twitter()
        self.assertTrue(twitter)

    def test_addMessage(self):
        #Given
        twitter =  Twitter()
        #When
        twitter.AddMessage('Hello')
        #Then
        self.assertEqual(twitter.tweets, ['Hello'])

if __name__ == '__main__':
    unittest.main()
