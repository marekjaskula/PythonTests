class Twitter(object):
    version ="1.0"

    def __init__(self):
        self.tweets = []

    def AddMessage(self, message):
        self.tweets.append(message)

twitter = Twitter()




twitter.AddMessage('Hello')
print(twitter.version, twitter.tweets)
