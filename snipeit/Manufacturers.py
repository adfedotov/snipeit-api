import requests as r

class Manufacturers():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self):
        """Get manufacturers

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/manufacturers'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_manufacturer_by_id(self, id: int):
        """Get manufacturer by id

        Args:
            id (int): Manufacturer id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/manufacturers/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, name: str):
        """Create manufacturer

        Args:
            name (str): Manufacturer name

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/manufacturers'

        payload = {
            'name': name
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, name: str):
        """Update manufacturer

        Args:
            id (int): Manufacturer id
            name (str): Manufacturer name

        Returns:
            dict: Json resposne
        """
        endpoint = f'{self.server}/api/v1/manufacturers/{id}'

        payload = {
            'name': name
        }

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete manufacturer

        Args:
            id (int): Manufacturer ID

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/manufacturers/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
    