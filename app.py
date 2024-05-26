from flask import Flask, render_template, request
from chatbot import get_gemini_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    chat_history = []
    if request.method == 'POST':
        user_input = request.form['input']
        response = get_gemini_response(user_input)
        response_text = "".join([chunk.text for chunk in response])
        chat_history.append(("You", user_input))
        chat_history.append(("Bot", response_text))

    return render_template('index.html', chat_history=chat_history)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
