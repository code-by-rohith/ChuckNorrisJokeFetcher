import requests

def fetch_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return data['value']

if __name__ == "__main__":
    joke = fetch_random_joke()
    print(joke)
