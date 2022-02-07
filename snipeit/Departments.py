import requests as r

class Departments():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self):
        endpoint = self.server + '/api/v1/departments'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        print(response.request)

        return response['rows']

    def get_department_by_id(self, id: int):
        endpoint = f'{self.server}/api/v1/departments/{id}'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        print(response.request)

        return response['rows']

    def create(self, name: str):
        endpoint = f'{self.server}/api/v1/departments'

        payload = {
            'name': name
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)
        response = response.json()

        print(response.request)

        return response['rows']

    def update(self, id: int, name: str):
        endpoint = f'{self.server}/api/v1/departments/{id}'

        payload = {
            'name': name
        }

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)
        response = response.json()

        print(response.request)

        return response['rows']

    def delete(self, id: int):
        endpoint = f'{self.server}/api/v1/departments/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)
        response = response.json()

        print(response.request)

        return response['rows']
    