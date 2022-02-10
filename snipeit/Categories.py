import requests as r

class Categories():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers
    
    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None):
        """Get categories

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the assets data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.

        Returns:
            dict: Json response
        """
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

        return response.json()

    def get_category_by_id(self, id: int):
        """Get category by id

        Args:
            id (int): Category id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/categories/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create category

        Args:
            payload (dict): Payload has to contain 'name', 'category_type'. Accepted:
                            # name (str),
                            # category_type (str) [asset, accessory, consumable, component],
                            # use_default_eula (bool, optional),
                            # require_acceptance (bool, optional),
                            # checkin_email (bool, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/categories'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update category

        Args:
            id (int): Category id
            payload (dict): Payload has to contain 'name', 'category_type'. Accepted:
                            # name (str),
                            # category_type (str) [asset, accessory, consumable, component],
                            # use_default_eula (bool, optional),
                            # require_acceptance (bool, optional),
                            # checkin_email (bool, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/categories/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete category

        Args:
            id (int): Category id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/categories/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
    