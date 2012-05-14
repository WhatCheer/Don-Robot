
class Memory(object):

    def __init__(self):
        raise NotImplementedError()

    def load(self, dump):
        raise NotImplementedError()

    def dump(self):
        raise NotImplementedError()

    def forget(self, key, conversation=None):
        raise NotImplementedError()

    def remember(self, key, value, conversation=None):
        raise NotImplementedError()

    def recall(self, key, conversation=None):
        raise NotImplementedError()
