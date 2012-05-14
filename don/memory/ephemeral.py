from don.memory import Memory as BaseMemory
import json

class Memory(BaseMemory):

    def __init__(self):
        self.me = {}
        self.conversations = {}

    def load(self, dump):
        obj = json.loads(dump)
        self.me = obj['me']
        self.conversations = obj['conversations']

    def dump(self):
        return json.dumps({"me":self.me,"conversations":self.conversations});

    def forget(self, key, conversation=None):
        try:
            if conversation:
                del self.conversations[conversation][key]
            else:
                del self.me[key]
        except:
            pass

    def remember(self, key, value, conversation=None):
        if conversation:
            if conversations not in self.conversations:
                self.conversations[conversation] = {}
            self.conversations[conversation][key] = value
        else:
            self.me[key] = value

    def recall(self, key, conversation=None):
        response = None

        if conversation:
            try:
                response = self.conversations[conversation][key]
            except:
                pass

        if not response:
            try:
                response = self.me[key]
            except:
                pass

        return response
