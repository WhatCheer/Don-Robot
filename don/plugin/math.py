from don.plugin import Plugin as BasePlugin
import re

class Plugin (BasePlugin):
    def __init__(self):
        self.strip = re.compile(r'( |\t|[ \t])+')
        self.math = re.compile(r'([0-9\+\*-/\(\)]+\.?[0-9\+\*-/\(\)]+)')
        self.mathexpr = re.compile(r'[\+\*-\/]')

    def respond(self, query):
        q = self.math.findall(self.strip.sub('', query))
        if 0 < len(q):
            response = []
            for group in q:
                if self.mathexpr.search(group):
                    try:
                        val = eval(group, {'__builtins__': None}, {})
                        response.append("{0} = {1}".format(group, val))
                    except:
                        pass

            if 0 < len(q):
                return "As far as I know, " + ', '.join(response)

        return False
