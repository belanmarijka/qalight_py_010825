import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, JSONDecodeError

base_url = "https://petstore.swagger.io/v2"

def get_pet(pet_id:int):
    r = None
    endpoint = "pet"
    try:
        response = requests.get(f"{base_url}/{endpoint}/{pet_id}")
        # response.raise_for_status()  # Викликає виняток, якщо код не 2xx але нам не треба, бо мб 400 і 404
        r = response.json()
    except (HTTPError, ConnectionError, Timeout, JSONDecodeError) as e:
        print(f"Exceptions: {e}")
    return r

def post_pet_id(pet_id:int, name:str):
    r = None
    endpoint = "pet"
    data = { 
        "name": name,
        "status": "available"
    }
    try:
        response = requests.post(f"{base_url}/{endpoint}/{pet_id}", data=data)
        # response.raise_for_status()  # Викликає виняток, якщо код не 2xx але нам не треба, бо мб 400 і 404
        r = response.json()
    except (HTTPError, ConnectionError, Timeout, JSONDecodeError) as e:
        print(f"Exceptions: {e}")
    return r

def post_pet(name:str):
    r = None
    endpoint = "pet"
    data = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
            }
    try:
        response = requests.post(f"{base_url}/{endpoint}", json=data)
        # response.raise_for_status()  # Викликає виняток, якщо код не 2xx але нам не треба, бо мб 400 і 404
        r = response.json()
    except (HTTPError, ConnectionError, Timeout, JSONDecodeError) as e:
        print(f"Exceptions: {e}")
    return r


def delete_pet(pet_id:int):
    r = None
    endpoint = "pet"
    try:
        response = requests.delete(f"{base_url}/{endpoint}/{pet_id}")
        # response.raise_for_status()  # Викликає виняток, якщо код не 2xx але нам не треба, бо мб 400 і 404
        r = response.json()
    except (HTTPError, ConnectionError, Timeout, JSONDecodeError) as e:
        print(f"Exceptions: {e}")
    return r


def autorizate_me(my_response):
    user_name = "user_name"
    password = "password"

    data = {
        "login":user_name,
        "secret":password
    }

    response = requests.post(f"{base_url}/auth", json=data)
    token = response.json().get("token")
    headers = my_response.headers
    headers['Authorization'] = f"Bearer {token}"
    my_response.headers = headers
    return my_response


if __name__ == "__main__":
    print(get_pet(9223372036854775807))
    print(get_pet(5))
    print(get_pet("derrere"))
    print(post_pet_id(5, "Patron"))
    print(delete_pet(5))
    print(post_pet("Patron"))
    