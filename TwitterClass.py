import re


class Twitter(object):
    version ="1.0"

    def __init__(self):
        self.tweets = []

    def AddMessage(self, message):
        if len(message) > 160:
            raise Exception("Wiadomośc przekracza 160 znaków")
        self.tweets.append(message)

    def findHashTags(self,messege):
        return re.findall("#(\w+ ", messege)

twitter = Twitter()




twitter.AddMessage('Hello')
print(twitter.version, twitter.tweets)
