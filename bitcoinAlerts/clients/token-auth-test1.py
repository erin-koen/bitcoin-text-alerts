import requests

local_host = "http://127.0.0.1:8000/api/"


def client():
    token_h = "Token 35a33a5ba22933d2be84b7e49e516ccb335b140d"
    headers = {
        "Authorization": token_h
    }
    response = requests.get(local_host+"profiles/", headers=headers)
    print("Status Code: ", response.status_code)
    response.data = response.json()
    print(response.data)


if __name__ == "__main__":
    client()
