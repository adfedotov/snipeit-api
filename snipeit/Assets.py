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

        return response.json()

    def get_asset_by_id(self, id: int):
        """Get asset by ID

        Args:
            id (int): ID of the asset to query

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}'
        
        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_asset_by_asset_tag(self, asset_tag: str):
        """Get asset by asset tag

        Args:
            asset_tag (str): Asset tag

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/bytag/{asset_tag}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_asset_by_serial(self, serial: str):
        """Get asset by serial

        Args:
            serial (str): Serial

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/byserial/{serial}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_assets_due_for_audit(self):
        """Get assets due for audit

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/audit/due'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_assets_overdue_for_audit(self):
        """Get assets overdue for audit

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/audit/overdue'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_asset_licenses(self, id: int):
        """Get a list of licenses for asset

        Args:
            id (int): Asset id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}/licenses'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create a new asset

        Args:
            payload (dict): Payload has to contain 'asset_tag', 'status_id', 'model_id'. Accepted:
                            # asset_tag (str),
                            # status_id (str),
                            # model_id (int),
                            # name (str, optional),
                            # image (file, optional),
                            # serial (str, optional),
                            # purchase_date (str, optional),
                            # purchase_cost (float, optional),
                            # order_number (str, optional),
                            # notes (str, optional),
                            # archived (bool, optional),
                            # requestable (bool, optional),
                            # warranty_months (int, optional),
                            # depreciate (bool, optional),
                            # supplier_id (int, optional),
                            # rtd_location_id (int, optional),
                            # last_audit_date (str, optional),
                            # location_id (int, optional),

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update asset

        Args:
            id (int): Asset id
            payload (dict): Payload has to contain 'asset_tag', 'status_id', 'model_id'. Accepted:
                            # asset_tag (str),
                            # status_id (str),
                            # model_id (int),
                            # name (str, optional),
                            # image (file, optional),
                            # serial (str, optional),
                            # purchase_date (str, optional),
                            # purchase_cost (float, optional),
                            # order_number (str, optional),
                            # notes (str, optional),
                            # archived (bool, optional),
                            # requestable (bool, optional),
                            # warranty_months (int, optional),
                            # depreciate (bool, optional),
                            # supplier_id (int, optional),
                            # rtd_location_id (int, optional),
                            # last_audit_date (str, optional),
                            # location_id (int, optional),
                            # last_checkout (str, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete asset

        Args:
            id (int): Asset id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()

    def checkout(self, id: int, payload: dict):
        """Checkout asset

        Args:
            id (int): Asset id
            payload (dict): Payload has to contain 'checkout_to_type'. Accepted:
                            # checkout_to_type (str) [user/asset/location],
                            # assigned_user (int, optional),
                            # assigned_asset (int, optional),
                            # assigned_location (int, optional),
                            # expected_checkin (str, optional),
                            # checkout_at (str, optional) [Override checkout date],
                            # name (str, optional) [New asset name],
                            # note (str, optional) 

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}/checkout'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def checkin(self, id: int, payload: dict={}):
        """Checkout asset

        Args:
            id (int): Asset id
            payload (dict): Payload. Accepted:
                            # note (str, optional)
                            # location_id (int, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/hardware/{id}/checkin'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()
