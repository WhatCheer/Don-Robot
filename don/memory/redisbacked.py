from don.memory import Memory as BaseMemory
import redis

class Memory(BaseMemory):

    def __init__(self, cfg={}, prefix="bot"):
        self.redis = redis.Redis(**cfg)
        self.prefix = prefix

    def load(self, dump):
        obj = json.loads(dump)
        for key,val in obj['me'].items():
            self.remember(key,val)
        for user,conversation in obj['conversations'].items():
            for key,val in conversation.items():
                self.remember(key, val, user)

    def dump(self):
        # TODO
        return

    def forget(self, key, conversation=None):
        try:
            if conversation:
                self.redis.hdel('%s:C:%s' % (self.prefix, conversation), key)
            else:
                self.redis.hdel('%s:ME' % self.prefix, key)
        except:
            pass

    def remember(self, key, value, conversation=None):
        if conversation:
            self.redis.sadd('%s:CONVERSATIONS' % self.prefix, conversation)
            self.redis.hset('%s:C:%s' % (self.prefix, conversation), key, value)
        else:
            self.redis.hset('%s:ME' % self.prefix, key, value)

    def recall(self, key, conversation=None):
        response = None

        if conversation:
            try:
                response = self.redis.hget('%s:C:%s' % (self.prefix, conversation), key)
            except:
                pass

        if not response:
            try:
                response = self.redis.hget('%s:ME' % self.prefix, key)
            except:
                pass

        return response
