import requests as r


class Assets():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self, limit: int=50, offset: int=None, search: str=None, order_number: str=None, sort: str=None, 
            order: str=None, model_id: int=None, category_id: int=None, manufacturer_id: int=None, company_id: int=None,
            location_id: int=None, status: str=None, status_id: int=None):
        """Return a list of assets

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the assets data for. Defaults to None.
            order_number (str, optional): Assets associated only with this order number. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.
            model_id (int, optional): Assets associated only with this model id. Defaults to None.
            category_id (int, optional): Assets associated only with this category id. Defaults to None.
            manufacturer_id (int, optional): Assets associated only with this manufacturer id. Defaults to None.
            company_id (int, optional): Assets associated only with this company id. Defaults to None.
            location_id (int, optional): Assets associated only with this location id. Defaults to None.
            status (str, optional): Assets associated only with this status. 'RTD', 'Deployed', 'Undeployable', 
                                    'Deleted', 'Archived', 'Requestable'. Defaults to None.
            status_id (int, optional): Assets associated only with this status id. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/hardware'

        endpoint += f'?limit={limit}'

        if offset is not None:
            endpoint += f'&offset={offset}'
        if search is not None:
            endpoint += f'&search={search}'
        if order_number is not None:
            endpoint += f'&order_number={order_number}'
        if sort is not None:
            endpoint += f'&sort={sort}'
        if order is not None:
            endpoint += f'&order={order}'
        if model_id is not None:
            endpoint += f'&model_id={model_id}'
        if category_id is not None:
            endpoint += f'&category_id={category_id}'
        if manufacturer_id is not None:
            endpoint += f'&manufacturer_id={manufacturer_id}'
        if company_id is not None:
            endpoint += f'&company_id={company_id}'
        if location_id is not None:
            endpoint += f'&location_id={location_id}'
        if status is not None:
            endpoint += f'&status={status}'
        if status_id is not None:
            endpoint += f'&status_id={status_id}'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_asset_by_id(self, id: int):
        """Get asset by ID

        Args:
            id (int): ID of the asset to query

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}'
        
        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_asset_by_asset_tag(self, asset_tag: str):
        """Get asset by asset tag

        Args:
            asset_tag (str): Asset tag

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/bytag/{asset_tag}'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_asset_by_serial(self, serial: str):
        """Get asset by serial

        Args:
            serial (str): Serial

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/byserial/{serial}'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_assets_due_for_audit(self):
        """Get assets due for audit

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/audit/due'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_assets_overdue_for_audit(self):
        """Get assets overdue for audit

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/audit/overdue'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def get_asset_licenses(self, id: int):
        """Get a list of licenses for asset

        Args:
            id (int): Asset id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}/licenses'

        response = r.request('GET', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def create(self, asset_tag: str, status_id: int, model_id: int, name: str=None, image=None, serial: str=None, purchase_date: str=None,
                purchase_cost: float=None, order_number: str=None, notes: str=None, archived: bool=False, warranty_months: int=None, 
                depreciate: bool=False, supplier_id: int=None, requestable: bool=False, rtd_location_id: int=None, last_audit_date: str=None, 
                location_id: int=None, custom_fields: dict=None):
        """Create a new asset

        Args:
            asset_tag (str): Asset tag
            status_id (int): Status id
            model_id (int): Model id
            name (str, optional): Asset name. Defaults to None.
            image ([type], optional): Asset image. Defaults to None.
            serial (str, optional): Serial number. Defaults to None.
            purchase_date (str, optional): Formatted purchase date. Defaults to None.
            purchase_cost (float, optional): Purchase cost. Defaults to None.
            order_number (str, optional): Order number. Defaults to None.
            notes (str, optional): Notes. Defaults to None.
            archived (bool, optional): is archived. Defaults to False.
            warranty_months (int, optional): Warranty in months. Defaults to None.
            depreciate (bool, optional): Defaults to False.
            supplier_id (int, optional): Supplier ID. Defaults to None.
            requestable (bool, optional): Is requestable. Defaults to False.
            rtd_location_id (int, optional): default location when not checked out. Defaults to None.
            last_audit_date (str, optional): Last audit formatted date. Defaults to None.
            location_id (int, optional): Location ID. Defaults to None.
            custom_fields (dict, optional): Dictionary of custom fields. Defaults to None.

        Returns:
            dict: Json response
        """

        endpoint = f'{self.server}/api/v1/hardware'

        payload = {
            'asset_tag': asset_tag,
            'status_id': status_id,
            'model_id': model_id,
            'name': name,
            'image': image,
            'serial': serial,
            'purchase_date': purchase_date,
            'purchase_cost': purchase_cost,
            'order_number': order_number,
            'notes': notes,
            'archived': archived,
            'requestable': requestable,
            'warranty_months': warranty_months,
            'depreciate': depreciate,
            'supplier_id': supplier_id,
            'rtd_location_id': rtd_location_id,
            'last_audit_date': last_audit_date,
            'location_id': location_id
        }

        for custom_field, value in custom_fields.items():
            payload[custom_field] = value

        response = r.request('POST', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def update(self, id: int, asset_tag: str, status_id: int, model_id: int, name: str=None, image=None, serial: str=None, purchase_date: str=None,
                purchase_cost: float=None, order_number: int=None, notes: str=None, archived: bool=False, warranty_months: int=None, 
                depreciate: bool=False, supplier_id: int=None, requestable: bool=False, rtd_location_id: int=None, last_audit_date: str=None, 
                location_id: int=None, last_checkout: str=None, custom_fields: dict=None):
        """Update asset information

        Args:
            id (int): Asset id
            asset_tag (str): Asset tag
            status_id (int): Status id
            model_id (int): Model id
            name (str, optional): Asset name. Defaults to None.
            image ([type], optional): Asset image. Defaults to None.
            serial (str, optional): Serial number. Defaults to None.
            purchase_date (str, optional): Formatted purchase date. Defaults to None.
            purchase_cost (float, optional): Purchase cost. Defaults to None.
            order_number (str, optional): Order number. Defaults to None.
            notes (str, optional): Notes. Defaults to None.
            archived (bool, optional): is archived. Defaults to False.
            warranty_months (int, optional): Warranty in months. Defaults to None.
            depreciate (bool, optional): Defaults to False.
            supplier_id (int, optional): Supplier ID. Defaults to None.
            requestable (bool, optional): Is requestable. Defaults to False.
            rtd_location_id (int, optional): default location when not checked out. Defaults to None.
            last_audit_date (str, optional): Last audit formatted date. Defaults to None.
            location_id (int, optional): Location ID. Defaults to None.
            last_checkout (str, optional): Last checked out formatted date. Defaults to None.
            custom_fields (dict, optional): Dictionary of custom fields. Defaults to None.

        Returns:
            dict: Json response
        """

        endpoint = f'{self.server}/api/v1/hardware/{id}'

        payload = {
            'asset_tag': asset_tag,
            'status_id': status_id,
            'model_id': model_id,
            'name': name,
            'image': image,
            'serial': serial,
            'purchase_date': purchase_date,
            'purchase_cost': purchase_cost,
            'order_number': order_number,
            'notes': notes,
            'archived': archived,
            'requestable': requestable,
            'warranty_months': warranty_months,
            'depreciate': depreciate,
            'supplier_id': supplier_id,
            'rtd_location_id': rtd_location_id,
            'last_audit_date': last_audit_date,
            'location_id': location_id,
            'last_checkout': last_checkout
        }

        for custom_field, value in custom_fields.items():
            payload[custom_field] = value

        response = r.request('PUT', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def partially_update(self, id, asset_tag=None, status_id=None, model_id=None, name=None, image=None, serial=None, purchase_date=None,
                purchase_cost=None, order_number=None, notes=None, archived=False, warranty_months=None, 
                depreciate=False, supplier_id=None, requestable=False, rtd_location_id=None, last_audit_date=None, 
                location_id=None, last_checkout=None, custom_fields=None):
        """Partially update asset information

        Args:
            id (int): Asset id
            asset_tag (str, optional): Asset tag. Defaults to None.
            status_id (int, optional): Status id. Defaults to None.
            model_id (int, optional): Model id. Defaults to None.
            name (str, optional): Asset name. Defaults to None.
            image ([type], optional): Asset image. Defaults to None.
            serial (str, optional): Serial number. Defaults to None.
            purchase_date (str, optional): Formatted purchase date. Defaults to None.
            purchase_cost (float, optional): Purchase cost. Defaults to None.
            order_number (str, optional): Order number. Defaults to None.
            notes (str, optional): Notes. Defaults to None.
            archived (bool, optional): is archived. Defaults to False.
            warranty_months (int, optional): Warranty in months. Defaults to None.
            depreciate (bool, optional): Defaults to False.
            supplier_id (int, optional): Supplier ID. Defaults to None.
            requestable (bool, optional): Is requestable. Defaults to False.
            rtd_location_id (int, optional): default location when not checked out. Defaults to None.
            last_audit_date (str, optional): Last audit formatted date. Defaults to None.
            location_id (int, optional): Location ID. Defaults to None.
            last_checkout (str, optional): Last checked out formatted date. Defaults to None.
            custom_fields (dict, optional): Dictionary of custom fields. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}'

        payload = {
            'asset_tag': asset_tag,
            'status_id': status_id,
            'model_id': model_id,
            'name': name,
            'image': image,
            'serial': serial,
            'purchase_date': purchase_date,
            'purchase_cost': purchase_cost,
            'order_number': order_number,
            'notes': notes,
            'archived': archived,
            'requestable': requestable,
            'warranty_months': warranty_months,
            'depreciate': depreciate,
            'supplier_id': supplier_id,
            'rtd_location_id': rtd_location_id,
            'last_audit_date': last_audit_date,
            'location_id': location_id,
            'last_checkout': last_checkout
        }

        for custom_field, value in custom_fields.items():
            payload[custom_field] = value

        response = r.request('PATCH', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def delete(self, id: int):
        """Delete asset

        Args:
            id (int): Asset id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)
        response = response.json()

        return response['rows']

    def checkout(self, id: int):
        pass

    def checkin(self, id: int):
        pass
