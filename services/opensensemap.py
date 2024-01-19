import requests
import json
from pprint import pprint

class OpenSenseMap:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def get_all_temperatures(self, method="GET", params=None, data=None):
        url = f"{self.base_url}/boxes?date={params}&phenomenon=temperature&format=json"
        response = requests.request(method, url, headers=self.headers, params=params, data=data)
        
        if response.status_code == 200:

            temperature_info = []

            data = response.json()
            
            for entry in data:                
                name = entry.get('name', 'Unknown Location')
                sensors = entry.get('sensors', [])

                for sensor in sensors:
                    if sensor.get('icon') == "osem-thermometer":

                        temperature_info.append({
                            'name': name,
                            'osem_temperature': {
                                'title': sensor.get('title', 'Unknown'),
                                'value': sensor.get('lastMeasurement', {}).get('value', 'N/A'),
                                'unit': sensor.get('unit', 'Celsius')
                            }
                        })
                    elif sensor.get('icon') == 'osem-temperature-celsius':
                        temperature_info.append({
                            'name': name,
                            'osem_temperature_celsius': {
                                'title': sensor.get('title', 'Unknown'),
                                'value': sensor.get('lastMeasurement', {}).get('value', 'N/A'),
                                'unit': sensor.get('unit', 'Celsius')
                            }
                        })

            result_json = json.dumps(temperature_info, indent=2)
            
            return result_json
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

                        # import code; code.interact(local=dict(globals(), **locals()))
