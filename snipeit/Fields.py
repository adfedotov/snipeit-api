import requests as r

class Fields():
    def __init__(self, server, headers):
        self.server = server
        self.headers = headers

    def get(self):
        """Get custom fields

        Returns:
            dict: Json response
        """
        endpoint = self.server + '/api/v1/fields'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def get_field_by_id(self, id: int):
        """Get field by id

        Args:
            id (int): field id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/fields/{id}'

        response = r.request('GET', endpoint, headers=self.headers)

        return response.json()

    def create(self, payload: dict):
        """Create field

        Args:
            payload (dict): Payload has to contain 'name', 'element'. Accepted:
                            # name (str)
                            # element (str) [text, textarea, checkbox, radio, listbox]
                            # field_values (str)
                            # show_in_email (bool)
                            # format (str)
                            # field_encrypted (bool)
                            # help_text (str)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/fields'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def update(self, id: int, payload: dict):
        """Update field

        Args:
            id (int): field ID
            Payload has to contain 'name', 'element'. Accepted:
                            # name (str)
                            # element (str) [text, textarea, checkbox, radio, listbox]
                            # field_values (str)
                            # show_in_email (bool)
                            # format (str)
                            # field_encrypted (bool)
                            # help_text (str)

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/fields/{id}'

        response = r.request('PUT', endpoint, headers=self.headers, json=payload)

        return response.json()

    def associate_with(self, id: int, fieldset_id: int):
        """Associate custom field with a custom fieldset

        Args:
            id (int): field id
            fieldset_id (int): fieldset id

        Returns:
            dict: Json response
        """
        payload = {
            'fieldset_id': fieldset_id
        }

        endpoint = f'{self.server}/api/v1/fields/{id}/associate'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def disassociate_with(self, id: int, fieldset_id: int):
        """Disassociate custom field with a custom fieldset

        Args:
            id (int): field id
            fieldset_id (int): fieldset id

        Returns:
            dict: Json response
        """
        payload = {
            'fieldset_id': fieldset_id
        }

        endpoint = f'{self.server}/api/v1/fields/{id}/disassociate'

        response = r.request('POST', endpoint, headers=self.headers, json=payload)

        return response.json()

    def delete(self, id: int):
        """Delete field

        Args:
            id (int): field id

        Returns:
            dict: Json response
        """
        endpoint = f'{self.server}/api/v1/fields/{id}'

        response = r.request('DELETE', endpoint, headers=self.headers)

        return response.json()
    