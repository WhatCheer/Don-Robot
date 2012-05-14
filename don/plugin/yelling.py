from don.plugin import Plugin as BasePlugin
import re
import random

class Plugin (BasePlugin):
    def __init__(self):
        self.noletters = re.compile(r'\W')
        self.yelling = re.compile(r'[A-Z]')

    def respond(self, query):
        q = self.noletters.sub('', query)
        notyelling = self.yelling.sub('', q)
        # If > 30% of the letters are caps, it's yelling.
        if len(q) and (float(len(notyelling)) / float(len(q))) < 0.3:
            return random.choice( (
                "Don't yell at me!",
                "Stop yelling!",
                "I don't like it when you yell!",
                "Don't yell, it makes my ears hurt!",
            ) )
        return False
