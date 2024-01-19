from flask import Flask, jsonify
from version import __version__
from services.opensensemap import OpenSenseMap
import json

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/version')
def home():
    return f'Your Flask App Version: {__version__}'


@app.route('/temperatures')
def temperatures():
    date_time = "2024-01-18T21:56:55Z"
    api = OpenSenseMap(base_url='https://api.opensensemap.org')
    data = json.loads(api.get_all_temperatures(params=date_time))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

            
