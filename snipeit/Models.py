import requests as r

class Models():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None):
        """Get models

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the models data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/models'

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

    def get_model_by_id(self, id: int):
        """Get model by id

        Args:
            id (int): model id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/models/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create model

        Args:
            payload (dict): Payload has to contain 'name', 'category_id', 'manufacturer_id'. Accepted:
                            # name (str)
                            # model_number (str, optional)
                            # category_id (int)
                            # manufacturer_id (int)
                            # eol (int, optional)
                            # fieldset_id (int, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/models'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update model

        Args:
            id (int): model id
            payload (dict): Payload has to contain 'name', 'category_id', 'manufacturer_id'. Accepted:
                            # name (str)
                            # model_number (str, optional)
                            # category_id (int)
                            # manufacturer_id (int)
                            # eol (int, optional)
                            # fieldset_id (int, optional)
                            # deprecation_id (int)
                            # notes (str)
                            # requestable (bool)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/models/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete model

        Args:
            id (int): model id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/models/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
