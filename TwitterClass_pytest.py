import pytest

from TwitterClass import Twitter


def test_TwitterClassMessage():
    twitter = Twitter()
    twitter.AddMessage('Hello')
    assert twitter.tweets == ['Hello']


def test_TwitterClassInit():
    twitter = Twitter()
    assert twitter

def test_longMessage():
    twitter = Twitter()
    with pytest.raises(Exception):
        twitter.AddMessage('test'*41)
    # print(twitter.tweets)
    assert twitter.tweets == []

def test_findHashTags():
    twitter = Twitter()
    message = 'Hello #first message'
    twitter.AddMessage(message)
    assert 'first' in twitter.findHashTags(message)

