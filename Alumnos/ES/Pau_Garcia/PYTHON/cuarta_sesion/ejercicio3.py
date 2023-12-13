import requests
def ranusr():
    response = requests.get("https://www.randomuser.me/api")
    random_users_data = response.json()
    first = random_users_data["results"][0]["name"]["first"]
    last = random_users_data["results"][0]["name"]["last"]
    print(f'The name of the user is {first} {last}.')

if __name__ == "__main__":
    ranusr()