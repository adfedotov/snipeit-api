import requests as r

class Users():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers
    
    def get(self, limit: int=50, offset: int=None, search: str=None, sort: str=None, order: str=None, first_name: str=None,
            last_name: str=None, username: str=None, email: str=None, employee_num: str=None, state: str=None, zip: str=None,
            country: str=None, group_id: int=None, department_id: int=None, company_id: int=None, location_id: int=None,
            deleted: bool=None, all: bool=None):
        """Get users

        Args:
            limit (int, optional): Number of entries to return. Defaults to 50.
            offset (int, optional): Offset to use. Defaults to None.
            search (str, optional): A text string to search the users data for. Defaults to None.
            sort (str, optional): Column to sort by. Defaults to None.
            order (str, optional): Order of sort 'asc' or 'desc'. Defaults to None.
            first_name (str, optional): First name. Defaults to None.
            last_name (str, optional): Last name. Defaults to None.
            username (str, optional): Username. Defaults to None.
            email (str, optional): Email. Defaults to None.
            employee_num (str, optional): Employee number. Defaults to None.
            state (str, optional): State. Defaults to None.
            zip (str, optional): Zip. Defaults to None.
            country (str, optional): Country. Defaults to None.
            group_id (int, optional): Group id. Defaults to None.
            department_id (int, optional): Department id. Defaults to None.
            company_id (int, optional): company id. Defaults to None.
            location_id (int, optional): locaton id. Defaults to None.
            deleted (bool, optional): Deleted user. Defaults to None.
            all (bool, optional): Both deleted and active. Defaults to None.

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/users'

        endpoint += f'?limit={limit}'

        if offset is not None:
            endpoint += f'&offset={offset}'
        if search is not None:
            endpoint += f'&search={search}'
        if sort is not None:
            endpoint += f'&sort={sort}'
        if order is not None:
            endpoint += f'&order={order}'
        if first_name is not None:
            endpoint += f'&first_name={first_name}'
        if last_name is not None:
            endpoint += f'&last_name={last_name}'
        if username is not None:
            endpoint += f'&username={username}'
        if email is not None:
            endpoint += f'&email={email}'
        if employee_num is not None:
            endpoint += f'&employee_num={employee_num}'
        if state is not None:
            endpoint += f'&state={state}'
        if zip is not None:
            endpoint += f'&zip={zip}'
        if country is not None:
            endpoint += f'&country={country}'
        if group_id is not None:
            endpoint += f'&group_id={group_id}'
        if department_id is not None:
            endpoint += f'&department_id={department_id}'
        if company_id is not None:
            endpoint += f'&company_id={company_id}'
        if location_id is not None:
            endpoint += f'&location_id={location_id}'
        if deleted is not None:
            endpoint += f'&deleted={deleted}'
        if all is not None:
            endpoint += f'&all={all}'
        
        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_user_by_id(self, id: int):
        """Get user by id

        Args:
            id (int): user id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_user_assets(self, id: int):
        """Get user's assets

        Args:
            id (int): user id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users/{id}/assets'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_user_accessories(self, id: int):
        """Get user's accessories

        Args:
            id (int): user id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users/{id}/accessories'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_user_licenses(self, id: int):
        """Get user's licenses

        Args:
            id (int): user id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users/{id}/licenses'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def me(self):
        """Get own user

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users/me'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create user

        Args:
            payload (dict): Payload has to contain 'first_name', 'username', 'password', 'password_confirmation'. Accepted:
                            # first_name (str),
                            # last_name (str, optional)
                            # username (str, optional),
                            # password (str, optional),
                            # password_confirmation (str, optional),
                            # email (str, optional),
                            # permissions (str, optional),
                            # activated (bool, optional),
                            # phone (str, optional),
                            # jobtitle (str, optional),
                            # manager_id (int, optional),
                            # employee_num (str, optional),
                            # notes (str, optional),
                            # company_id (int, optional),
                            # two_factor_enrolled (bool, optional),
                            # two_factor_optin (bool, optional),
                            # department_id (int, optional),
                            # location_id (int, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update user

        Args:
            id (int): user id
            payload (dict): Payload. Accepted:
                            # first_name (str),
                            # last_name (str, optional)
                            # username (str, optional),
                            # password (str, optional),
                            # email (str, optional),
                            # permissions (str, optional),
                            # activated (bool, optional),
                            # phone (str, optional),
                            # jobtitle (str, optional),
                            # manager_id (int, optional),
                            # employee_num (str, optional),
                            # notes (str, optional),
                            # company_id (int, optional),
                            # two_factor_enrolled (bool, optional),
                            # two_factor_optin (bool, optional),
                            # department_id (int, optional),
                            # location_id (int, optional)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete user

        Args:
            id (int): user id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/users/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
