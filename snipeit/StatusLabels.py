import requests as r

class StatusLabels():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None):
        """Get statuslabels

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the statuslabels data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/statuslabels'

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

    def get_statuslabel_by_id(self, id: int):
        """Get statuslabel by id

        Args:
            id (int): statuslabel id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/statuslabels/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_statuslabel_assets(self, id: int):
        """Get asset list under statuslabel

        Args:
            id (int): statuslabel id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/statuslabels/{id}/assetlist'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create statuslabel

        Args:
            payload (dict): Payload has to contain 'name'. Accepted:
                            # name (str),
                            # type (str, optional) [deployable, pending, archived]
                            # notes (str, optional),
                            # show_in_nav (bool, optional),
                            # default_label (bool, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/statuslabels'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update statuslabel

        Args:
            id (int): statuslabel id
            payload (dict): Payload has to contain 'name'. Accepted:
                            # name (str),
                            # type (str, optional) [deployable, pending, archived]
                            # notes (str, optional),
                            # show_in_nav (bool, optional),
                            # default_label (bool, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/statuslabels/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete statuslabel

        Args:
            id (int): statuslabel id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/statuslabels/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
