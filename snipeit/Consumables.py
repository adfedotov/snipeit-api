import requests as r

class Consumables():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None, order_number: str=None, 
            expand: str=None, category_id: int=None, company_id: int=None, manufacturer_id: int=None):
        """Get consumables

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the consumables data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.
            order_number (str, optional): consumables associated only with this order number. Defaults to None.
            expand (str, optional): Show additional details. Defaults to None.
            category_id (int, optional): consumables associated only with this category id. Defaults to None.
            manufacturer_id (int, optional): consumables associated only with this manufacturer id. Defaults to None.
            company_id (int, optional): consumables associated only with this company id. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/consumables'

        endpoint += f'?limit={limit}'

        if offset is not None:
            endpoint += f'&offset={offset}'
        if search is not None:
            endpoint += f'&search={search}'
        if sort is not None:
            endpoint += f'&sort={sort}'
        if order is not None:
            endpoint += f'&order={order}'
        if order_number is not None:
            endpoint += f'&order_number={order_number}'
        if expand is not None:
            endpoint += f'&expand={expand}'
        if category_id is not None:
            endpoint += f'&category_id={category_id}'
        if company_id is not None:
            endpoint += f'&company_id={company_id}'
        if manufacturer_id is not None:
            endpoint += f'&manufacturer_id={manufacturer_id}'
        
        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_consumable_by_id(self, id: int):
        """Get consumable by id

        Args:
            id (int): consumable id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/consumables/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create consumable

        Args:
            payload (dict): Payload has to contain 'name', 'qty', 'category_id'. Accepted:
                            # name (str),
                            # qty (int),
                            # category_id (int),
                            # order_number (str, optional)
                            # purchase_cost (float, optional),
                            # purchase_date (str, optional),
                            # model_number (int, optional),
                            # company_id (int, optional),
                            # location_id (int, optional),
                            # manufacturer_id (int, optional),
                            # supplier_id (int, optional),
                            # min_amt (int, optional),
                            # item_no (str, optional)
                            # requestable (bool, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/consumables'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update consumable

        Args:
            id (int): consumable id
            payload (dict): Payload has to contain 'name', 'qty', 'category_id'. Accepted:
                            # name (str),
                            # qty (int),
                            # category_id (int),
                            # order_number (str, optional)
                            # purchase_cost (float, optional),
                            # purchase_date (str, optional),
                            # model_number (int, optional),
                            # company_id (int, optional),
                            # location_id (int, optional),
                            # manufacturer_id (int, optional),
                            # supplier_id (int, optional),
                            # min_amt (int, optional),
                            # item_no (str, optional)
                            # requestable (bool, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/consumables/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete consumable

        Args:
            id (int): consumable id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/consumables/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()

    def checkout(self, id: int, assigned_to: int=None):
        """Checkout consumable

        Args:
            id (int): consumable id
            assigned_to (int, optional): Assigned to person ID

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/consumables/{id}/checkout'

        payload = {
            'assigned_to': assigned_to
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def checkin(self, id: int):
        """Checkin consumable

        Args:
            id (int): consumable id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/consumables/{id}/checkin'

        response = r.request('POST', endpoint, headers=self.headers)

        return response.json()
