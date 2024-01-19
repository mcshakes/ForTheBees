from flask import Flask
from version import __version__
from services.opensensemap import OpenSenseMap

app = Flask(__name__)

@app.route('/version')
def home():
    return f'Your Flask App Version: {__version__}'


@app.route('/temperatures')
def temperatures():
    date_time = "2024-01-18T21:56:55Z"
    api = OpenSenseMap(base_url='https://api.opensensemap.org')
    data = api.get_all_temperatures(params=date_time)
    return data

if __name__ == '__main__':
    app.run(debug=True)
    
# import code; code.interact(local=dict(globals(), **locals()))