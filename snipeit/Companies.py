import requests as r

class Companies():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self):
        endpoint = self.server + '/api/v1/companies'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_company_by_id(self, id: int):
        endpoint = f'{self.server}/api/v1/companies/{id}'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def create(self, name: str):
        endpoint = f'{self.server}/api/v1/companies'

        payload = {
            'name': name
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def update(self, id: int, name: str):
        endpoint = f'{self.server}/api/v1/companies/{id}'

        payload = {
            'name': name
        }

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def delete(self, id: int):
        endpoint = f'{self.server}/api/v1/companies/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']
    