import requests


class QueueClient:
    def __init__(self, base_url, token=None):
        self._base_url = base_url
        self._token = token

    def set_token(self, token):
        self._token = token

    def authenticate(self, username, password):
        auth_url = f"{self._base_url}/users/login"
        response = requests.post(auth_url, json={"username": username, "password": password})
        if response.status_code == 200:
            self._token = response.json().get("token")
            return self._process_response(response)
        else:
            print("Authentication failed: HTTP status code " + str(response.status_code))

    def send_code(self, code):
        return self._request_with_token('post', '/tasks', json={"code": code})

    def get_result(self):
        return self._request_with_token('get', '/tasks/result')

    def get_queue_position(self):
        return self._request_with_token('get', '/tasks/queue-position')

    def cancel_task(self):
        return self._request_with_token('delete', '/tasks/cancel')

    def _request_with_token(self, method, endpoint, **kwargs):
        if not self._token:
            raise Exception("No token provided. Please set the token or authenticate first.")

        headers = {'Authorization': f"{self._token}"}
        response = requests.request(method, f"{self._base_url}{endpoint}", headers=headers, **kwargs)
        return self._process_response(response)

    @staticmethod
    def _process_response(response):
        def print_json(data_json, indent=0):
            print("Response:")
            for key, value in data_json.items():
                if isinstance(value, dict):
                    print(' ' * indent + f"{key}:")
                    print_json(value, indent + 4)
                else:
                    print(' ' * indent + f"{key}: {value}")

        data = response.json()
        print_json(data)
