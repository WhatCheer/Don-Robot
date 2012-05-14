import json
import don
import don.memory.ephemeral

import don.plugin.yelling
import don.plugin.math

mem = don.memory.ephemeral.Memory()
bot = don.Don(mem)

bot.addPlugin(don.plugin.yelling.Plugin())
bot.addPlugin(don.plugin.math.Plugin())

for f in ['swear', 'don', 'hello', 'jokes', 'clever', 'lastresort']:
    with open('brains/%s.json' % f, 'r') as handle:
        bot.loadBrain(json.loads(handle.read()));

try:
    while True:
        query = raw_input("> ")
        print 'don>', bot.converse(query,'testing')
except Exception, e:
    print e
    pass
