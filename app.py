from flask import Flask, render_template, request, jsonify
from chatbot import get_gemini_response
import sys
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def home():
    chat_history = []
    if request.method == 'POST':
        user_input = request.form['msg']
        response = get_gemini_response(user_input)
        bot_response = "".join([chunk.text for chunk in response])
        chat_history.append(("You", user_input))
        chat_history.append(("Bot", bot_response))
        print(bot_response, file=sys.stderr)

        return jsonify(bot_response=bot_response)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
