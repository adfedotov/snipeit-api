import requests as r

class Categories():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers
    
    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None):
        endpoint = self.server + '/api/v1/categories'

        endpoint += f'?limit={limit}'

        if offset is not None:
            endpoint += f'&offset={offset}'
        if search is not None:
            endpoint += f'&search={search}'
        if sort is not None:
            endpoint += f'&sort={sort}'
        if order is not None:
            endpoint += f'&order={order}'
        
        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_category_by_id(self, id: int):
        endpoint = f'{self.server}/api/v1/categories/{id}'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def create(self, name: str, category_type: str, use_default_eula: bool=None, require_acceptance: bool=None, checkin_email: bool=None):
        endpoint = f'{self.server}/api/v1/categories'

        payload = {
            'name': name,
            'category_type': category_type,
            'use_default_eula': use_default_eula,
            'require_acceptance': require_acceptance,
            'checkin_email': checkin_email
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def update(self, id: int, name: str, category_type: str, use_default_eula: bool=None, require_acceptance: bool=None, checkin_email: bool=None):
        endpoint = f'{self.server}/api/v1/categories/{id}'

        payload = {
            'name': name,
            'category_type': category_type,
            'use_default_eula': use_default_eula,
            'require_acceptance': require_acceptance,
            'checkin_email': checkin_email
        }

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def partially_update(self, id: int, name: str, category_type: str, use_default_eula: bool=None, require_acceptance: bool=None, checkin_email: bool=None):
        endpoint = f'{self.server}/api/v1/categories/{id}'

        payload = {
            'name': name,
            'category_type': category_type,
            'use_default_eula': use_default_eula,
            'require_acceptance': require_acceptance,
            'checkin_email': checkin_email
        }

        response = r.request('PATCH', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def delete(self, id: int):
        endpoint = f'{self.server}/api/v1/categories/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']
    