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
    users = []
    
    i = 0
    while len(users) != n:
        response = requests.get(url)
        if response.status_code == 200:
            user = response.json()['results'][0]
            if user['gender'] == gender:
                users.append(user)
        i += 1
        
    print(i)
    return users


print(get_randomusers(5, 'female'))
