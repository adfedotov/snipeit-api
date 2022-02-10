import requests as r

class Locations():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None):
        """Get locations

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the locations data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/locations'

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

        return response.json()

    def get_location_by_id(self, id: int):
        """Get location by id

        Args:
            id (int): location id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/locations/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create location

        Args:
            payload (dict): Payload has to contain 'name'. Accepted:
                            # name (str),
                            # address (str, optional),
                            # address2 (str, optional),
                            # state (str, optional),
                            # country (str, optional),
                            # zip (str, optional),
                            # ldap_ou (str, optional),
                            # parent_id (int, optional),
                            # currency (str, optional),
                            # manager_id (int, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/locations'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update location

        Args:
            id (int): location id
            payload (dict): Payload has to contain 'name'. Accepted:
                            # name (str),
                            # address (str, optional),
                            # address2 (str, optional),
                            # state (str, optional),
                            # country (str, optional),
                            # zip (str, optional),
                            # ldap_ou (str, optional),
                            # parent_id (int, optional),
                            # currency (str, optional),
                            # manager_id (int, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/locations/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete location

        Args:
            id (int): location id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/locations/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
