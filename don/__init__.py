import re
import random
import os

class Don (object):

    def __init__(self, memory):
        self.brains = []
        self.memory = memory
        self.plugins = []

        try:
            random.seed(os.urandom(32))
        except:
            pass

        self.debug = False

        self.strip = re.compile(r'( |\t|[ \t])+')
        self.subs = re.compile(r'\<(.*?)\>')
        self.gets = re.compile(r'\<get:(.*?)\>')

    def addPlugin(self, plugin):
      self.plugins.append(plugin)

    def preProcessMatch(self, entry):
        entry = entry.replace('<*>', '(\\b\w*\\b)')
        for match in self.subs.findall(entry):
            entry = entry.replace('<%s>' % match, '(?P<%s>\\b\w+\\b)' % match)
        return entry

    def know(self, match, response, remember=None, fail=None):
        try:
            regx = re.compile(self.preProcessMatch(match), re.IGNORECASE)
            self.brains.append((regx, response, remember, fail))
        except Exception, e:
            print "ERROR - Could not know:", match, "because:", e

    def loadBrain(self, brain):
        for entry in brain:
            remember = None
            fail = None
            if 'remember' in entry:
                remember = entry['remember']
            if 'fail' in entry:
                fail = entry['fail']
            self.know(entry['match'], entry['response'], remember, fail)

    def respond(self, responses, match, remember=None, conversation=None, fail=None):
        if list == type(responses):
            response = random.choice(responses)
        else:
            response = responses

        # Store memory
        if remember and conversation:
            for key in remember:
                    self.memory.remember(key, match.group(key), conversation)

        # Named groups
        for group,value in match.groupdict().items():
            response = response.replace('<%s>' % group, value)

        # Numbered groups
        for group in range(1,10):
            try:
                response = response.replace('<%d>' % (group - 1), match.group(group))
            except:
                break

        # Memory groups
        for match in self.gets.findall(response):
            memory = self.memory.recall(match, conversation)
            if memory:
                response = response.replace('<get:%s>' % match, memory)

        # We cannot return anything with un-substituted values.
        if self.subs.search(response):
            response = None

        if not response:
            if list == type(fail):
                response = random.choice(fail)
            else:
                response = fail

        return response

    def converse(self, query, conversation=None):
        for plugin in self.plugins:
          response = plugin.respond(query)
          if False != response:
              return response

        query = self.strip.sub(' ', query)
        response = None
        for knowledge in self.brains:
            matched = knowledge[0].search(query)
            if matched:
                response = self.respond(knowledge[1], matched, knowledge[2], conversation, knowledge[3])
                if response:
                    break

        return response

    def amnesia(self):
        self.brain = []
