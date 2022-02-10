import requests as r

class Companies():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self):
        """Get companies

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/companies'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_company_by_id(self, id: int):
        """Get company by id

        Args:
            id (int): Company id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/companies/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, name: str):
        """Create company

        Args:
            name (str): Company name

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/companies'

        payload = {
            'name': name
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, name: str):
        """Update company

        Args:
            id (int): Company id
            name (str): Company name

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/companies/{id}'

        payload = {
            'name': name
        }

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete company

        Args:
            id (int): Company id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/companies/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
    