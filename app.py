from flask import Flask, request, make_response, render_template

import json

import don
import don.memory.redisbacked

app = Flask(__name__)

mem = don.memory.redisbacked.Memory()
bot = don.Don(mem)

for f in ['swear', 'don', 'hello', 'jokes', 'clever', 'lastresort']:
    with open('brains/%s.json' % f, 'r') as handle:
        bot.loadBrain(json.loads(handle.read()));

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/chat.txt")
def chat():
    body = request.args.get('body')
    convo = request.args.get('conversation')
    if not body:
        resp = make_response("body is required", 400)
    else:
        if not convo:
            resp = make_response("conversation is required", 400)
        else:
            reply = bot.converse(body, convo)
            if reply:
                resp = make_response(reply, 200)
            else:
                resp = make_response("That does not compute.", 200)

    resp.headers['Content-Type'] = 'text/plain'
    return resp

if __name__ == "__main__":
    app.run()
