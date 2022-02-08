import requests as r

class Accessories():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None, order_number: str=None, expand: str=None):
        """Get accessories

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the assets data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.
            order_number (str, optional): Accessories associated only with this order number. Defaults to None.
            expand (str, optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        endpoint = self.server + '/api/v1/accessories'

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
            endpoint += f'&order_number={expand}'
        
        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_accessory_by_id(self, id: int):
        """Get accessory by id

        Args:
            id (int): Accessory id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/accessories/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def checkedout(self, id: int):
        endpoint = f'{self.server}/api/v1/accessories/{id}/checkedout'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create accessory

        Args:
            payload (dict): Payload has to contain 'name', 'qty', 'category_id'. Accepted:
                            # 'name': name,
                            # 'qty': qty,
                            # 'category_id': category_id,
                            # 'order_number': order_number,
                            # 'purchase_cost': purchase_cost,
                            # 'purchase_date': purchase_date,
                            # 'model_number': model_number,
                            # 'company_id': company_id,
                            # 'location_id': location_id,
                            # 'manufacturer_id': manufacturer_id,
                            # 'supplier_id': supplier_id,
                            # 'image': image,
                            # 'min_amt': min_amt,
                            # 'requestable': requestable

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/accessories'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update accessory

        Args:
            id (int): Accessory id
            payload (dict): Payload has to contain 'name', 'qty', 'category_id'. Accepted:
                            # 'name': name,
                            # 'qty': qty,
                            # 'category_id': category_id,
                            # 'order_number': order_number,
                            # 'purchase_cost': purchase_cost,
                            # 'purchase_date': purchase_date,
                            # 'model_number': model_number,
                            # 'company_id': company_id,
                            # 'location_id': location_id,
                            # 'manufacturer_id': manufacturer_id,
                            # 'supplier_id': supplier_id,
                            # 'image': image,
                            # 'min_amt': min_amt,
                            # 'requestable': requestable

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/accessories/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete accessory

        Args:
            id (int): Accessory id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/accessories/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
