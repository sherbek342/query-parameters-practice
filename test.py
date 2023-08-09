import requests


url = 'https://randomuser.me/api/'


def get_randomusers(n: int, gender: str) -> list:
    '''Random User Generator allows you to fetch up to 5,000\
         generated users in one request using the results parameter.
    
    Args:
        n (int): number of users
    
    Returns:
        list: lsit of users
    '''
    url = f'{url}?results={n}&gender={gender}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['results']


print(get_randomusers(5, 'female'))
