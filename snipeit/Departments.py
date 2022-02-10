import requests as r

class Departments():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self):
        """Get departments

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/departments'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_department_by_id(self, id: int):
        """Get department by id

        Args:
            id (int): Deparment id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/departments/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, name: str):
        """Create department

        Args:
            name (str): Department name

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/departments'

        payload = {
            'name': name
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, name: str):
        """Update department

        Args:
            id (int): Department ID
            name (str): Department name

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/departments/{id}'

        payload = {
            'name': name
        }

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete department

        Args:
            id (int): Department id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/departments/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
    