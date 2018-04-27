from TwitterClass import Twitter


def test_TwitterClassMessage():
    twitter = Twitter()
    twitter.AddMessage('Hello')
    assert twitter.tweets == ['Hello']


def test_TwitterClassInit():
    twitter = Twitter()
    assert twitter

def test_longMNessage():
    twitter = Twitter()
    twitter.AddMessage('test'*31)
    # print(twitter.tweets)
    # assert twitter.tweets == ['test'*1]


