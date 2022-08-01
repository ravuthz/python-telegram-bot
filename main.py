from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    import telegram_bot
    return "hello from flask app"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="80")
