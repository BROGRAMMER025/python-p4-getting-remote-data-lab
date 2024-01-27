
import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: {response.status_code}"
        except requests.RequestException as e:
            return f"Error: {e}"

    def load_json(self):
        response_body = self.get_response_body()
        try:
            
            json_data = json.loads(response_body)
            return json_data
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"


url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)


response_body = requester.get_response_body()
print("Response Body:")
print(response_body)


json_data = requester.load_json()
print("\nJSON Data:")
print(json_data)