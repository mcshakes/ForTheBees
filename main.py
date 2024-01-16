from flask import Flask
from version import __version__

app = Flask(__name__)

@app.route('/version')
def home():
    return f'Your Flask App Version: {__version__}'


@app.route('/temperature')
def temperature():
    return f'poop'

if __name__ == '__main__':
    app.run(debug=True)
