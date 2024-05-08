import requests
print("mrow")
class ILOVECATS:
    def __init__(self):
        print("I love cats!")
    def get_cat(self):
        url = 'https://cataas.com/cat'
        response = requests.get(url)
        with open('cat.jpg', 'wb') as file:
            file.write(response.content)
