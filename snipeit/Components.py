import requests as r

class Components():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None, order_number: str=None, expand: str=None):
        """Get components

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the assets data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.
            order_number (str, optional): Components associated only with this order number. Defaults to None.
            expand (str, optional): [description]. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/components'

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
        
        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_component_by_id(self, id: int):
        """Get component by id

        Args:
            id (int): component id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/components/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def assets(self, id: int):
        """Show which assets a components has been assigned to

        Args:
            id (int): component id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/components/{id}/assets'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create component

        Args:
            payload (dict): Payload has to contain 'name', 'qty', 'category_id'. Accepted:
                            # name (str),
                            # qty (int),
                            # category_id (int),
                            # order_number (str, optional)
                            # purchase_cost (float, optional),
                            # purchase_date (str, optional),
                            # company_id (int, optional),
                            # location_id (int, optional),
                            # min_amt (int, optional),
                            # serial (str, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/components'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update component

        Args:
            id (int): component id
            payload (dict): Payload has to contain 'name', 'qty', 'category_id'. Accepted:
                            # name (str),
                            # qty (int),
                            # category_id (int),
                            # order_number (str, optional)
                            # purchase_cost (float, optional),
                            # purchase_date (str, optional),
                            # company_id (int, optional),
                            # location_id (int, optional),
                            # min_amt (int, optional),
                            # serial (str, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/components/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete component

        Args:
            id (int): component id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/components/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()

    def checkout(self, id: int, payload: dict):
        """Checkout component

        Args:
            id (int): component id
            payload (dict): Payload has to contain 'assigned_to' and 'assigned_qty'. Accepted:
                            # assigned_to (int) [user],
                            # assigned_qty (int)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/components/{id}/checkout'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def checkin(self, id: int, checkin_qty: int):
        """Checkin component

        Args:
            id (int): component id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/components/{id}/checkin'

        payload = {
            'checkin_qty': checkin_qty
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()
