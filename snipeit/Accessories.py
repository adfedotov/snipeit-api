import requests as r

class Accessories():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None, order_number: str=None, expand: str=None):
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
        response = response.json()

        return response['rows']

    def get_accessory_by_id(self, id: int):
        endpoint = f'{self.server}/api/v1/accessories/{id}'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def checkedout(self, id: int):
        endpoint = f'{self.server}/api/v1/accessories/{id}/checkedout'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def create(self, name: str, qty: int, category_id: int, order_number: str=None, purchase_cost: float=None, purchase_date: str=None, model_number: str=None,
                company_id: int=None, location_id: int=None, manufacturer_id: int=None, supplier_id: int=None, image=None, min_amt: int=None, requestable: bool=None):
        endpoint = f'{self.server}/api/v1/accessories'

        # some of this stuff might not be handled by SnipeIT API
        payload = {
            'name': name,
            'qty': qty,
            'category_id': category_id,
            'order_number': order_number,
            'purchase_cost': purchase_cost,
            'purchase_date': purchase_date,
            'model_number': model_number,
            'company_id': company_id,
            'location_id': location_id,
            'manufacturer_id': manufacturer_id,
            'supplier_id': supplier_id,
            'image': image,
            'min_amt': min_amt,
            'requestable': requestable
        }

        response = r.request('POST', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def update(self, id: int, name: str, qty: int, category_id: int, order_number: str=None, purchase_cost: float=None, purchase_date: str=None, 
                model_number: str=None, company_id: int=None, location_id: int=None, manufacturer_id: int=None, supplier_id: int=None, 
                image=None, min_amt: int=None, requestable: bool=None):
        endpoint = f'{self.server}/api/v1/accessories/{id}'

        # some of this stuff might not be handled by SnipeIT API
        payload = {
            'name': name,
            'qty': qty,
            'category_id': category_id,
            'order_number': order_number,
            'purchase_cost': purchase_cost,
            'purchase_date': purchase_date,
            'model_number': model_number,
            'company_id': company_id,
            'location_id': location_id,
            'manufacturer_id': manufacturer_id,
            'supplier_id': supplier_id,
            'image': image,
            'min_amt': min_amt,
            'requestable': requestable
        }

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def partially_update(self, id: int, name: str=None, qty: int=None, category_id: int=None, order_number: str=None, purchase_cost: float=None, purchase_date: str=None, 
                            model_number: str=None, company_id: int=None, location_id: int=None, manufacturer_id: int=None, supplier_id: int=None, 
                            image=None, min_amt: int=None, requestable: bool=None):
        endpoint = f'{self.server}/api/v1/accessories/{id}'

        # some of this stuff might not be handled by SnipeIT API
        payload = {
            'name': name,
            'qty': qty,
            'category_id': category_id,
            'order_number': order_number,
            'purchase_cost': purchase_cost,
            'purchase_date': purchase_date,
            'model_number': model_number,
            'company_id': company_id,
            'location_id': location_id,
            'manufacturer_id': manufacturer_id,
            'supplier_id': supplier_id,
            'image': image,
            'min_amt': min_amt,
            'requestable': requestable
        }

        response = r.request('PATCH', endpoint, headers=self.headers, json=payload)
        response = response.json()

        return response['rows']

    def delete(self, id: int):
        endpoint = f'{self.server}/api/v1/accessories/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']
