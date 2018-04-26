class Twitter(object):
    version ="1.0"

    def __init__(self):
        self.tweets = []


user = Twitter()
print(user.version, user.tweets)
