import requests
import json


class RandomUser:
    def __init__(self) -> None:
        self.url = 'https://randomuser.me/api/'

    def get_randomusers(self, n: int) -> list:
        '''Random User Generator allows you to fetch up to 5,000\
             generated users in one request using the results parameter.
        
        Args:
            n (int): number of users
        
        Returns:
            list: lsit of users
        '''
        payload = {
            'results': n
        }
        response = requests.get(url=self.url, params=payload)
        if response.status_code == 200:
            return response.json()['results']

        return False
    
    def get_user_by_gender(self, gender: str) -> dict:
        '''return specify whether only male or only female users generated.\
            Valid values for the gender parameter are "male" or "female"

        Args:
            gender (str): gender (female or male)
        
        Returns:
            str: user
        '''
        pass
    
    def get_users_by_gender(self, n: int, gender: str) -> dict:
        '''return specify whether only male or only female users generated.\
            Valid values for the gender parameter are "male" or "female"

        Args:
            n (int): number of users
            gender (str): gender (female or male)
        
        Returns:
            str: user
        '''
        pass
    
    def get_user_by_nat(self, nat: str) -> dict:
        '''get user nationality from randomuser

        Args:
            nat (str): user nationality
        
        Returns:
            str: user
        '''
        pass
    
    def get_users_by_nat(self, n: int, nat: str) -> dict:
        '''get user nationality from randomuser

        Args:
            n (int): number of users
            nat (str): user nationality
        
        Returns:
            str: user
        '''
        pass
    
    def get_specific_field(self, field: str) -> dict:
        '''get user specific field from randomuser

        Note:
            including fields: gender, name, location, email, login, registered, dob, phone, cell, id, picture, nat

        Args:
            field (str): specific field
        
        Returns:
            dict: data
        '''
        pass
    
    def get_users_specific_field(self, n: int, field: str) -> list:
        '''get user specific field from randomuser

        Note:
            including fields: gender, name, location, email, login, registered, dob, phone, cell, id, picture, nat

        Args:
            n (int): number of users
            field (str): specific field
        
        Returns:
            lsit: list of user data
        '''
        pass


r = RandomUser()
with open('users.json', 'w') as f:
    json.dump(r.get_randomusers(5), f, indent=4)
    