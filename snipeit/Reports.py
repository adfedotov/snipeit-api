import requests as r

class Reports():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, target_type: str=None, target_id: int=None,
            item_type: str=None, item_id: int=None, action_type: str=None):
        """Get consumables

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the consumables data for. Defaults to None.
            target_type (str, optional): Type of traget checked out to (App/Model/User). Defaults to None.
            target_id (int, optional): ID of target. Defaults to None.
            item_type (str, optiona): Type of item (App/Model/Asset). Defaults to None.
            item_id (int, optional): ID of item. Defaults to None.
            action_type (str, optional): Type of action (checkin from, checkout, update, add seats, etc.). Defaults to None

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/consumables'

        endpoint += f'?limit={limit}'

        if offset is not None:
            endpoint += f'&offset={offset}'
        if search is not None:
            endpoint += f'&search={search}'
        if target_type is not None:
            endpoint += f'&target_type={target_type}'
        if target_id is not None:
            endpoint += f'&target_id={target_id}'
        if item_type is not None:
            endpoint += f'&item_type={item_type}'
        if item_id is not None:
            endpoint += f'&item_id={item_id}'
        if action_type is not None:
            endpoint += f'&action_type={action_type}'
        
        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()