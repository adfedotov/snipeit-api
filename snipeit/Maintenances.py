import requests as r

class Maintenances():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None, asset_id: int=None):
        """Get maintenances

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the maintenances data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.
            asset_id (int, optional): Asset ID. Defaults to None

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/maintenances'

        endpoint += f'?limit={limit}'

        if offset is not None:
            endpoint += f'&offset={offset}'
        if search is not None:
            endpoint += f'&search={search}'
        if sort is not None:
            endpoint += f'&sort={sort}'
        if order is not None:
            endpoint += f'&order={order}'
        if asset_id is not None:
            endpoint += f'&asset_id={asset_id}'
        
        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create maintenance

        Args:
            payload (dict): Payload has to contain 'title', 'asset_id', 'supplier_id', 'start_date'. Accepted:
                            # title (str)
                            # asset_id (str)
                            # supplier_id (str)
                            # is_warranty (bool, optional)
                            # cost (float, optional)
                            # notes (str, optional)
                            # asset_mainenance_type (str, optional) [Maintenance/Repair/PAT Test/Upgrade/Hardware Support/Software Support
                            # completion_date (str, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/maintenances'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        # Can't update?
        pass

    def delete(self, id: int):
        """Delete maintenance

        Args:
            id (int): maintenance id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/maintenances/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
