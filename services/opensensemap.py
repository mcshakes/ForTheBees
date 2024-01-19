import requests

class OpenSenseMap:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def get_all_temperatures(self, method="GET", params=None, data=None):
        url = f"{self.base_url}/boxes?date={params}&phenomenon=temperature&format=json"
        response = requests.request(method, url, headers=self.headers, params=params, data=data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

