from bs4 import BeautifulSoup
import requests
import json

url = "https://quotes.toscrape.com/"

result = requests.get(url)
quotes = BeautifulSoup(result.text,"html.parser")

dict = {}
for i in range(2,7):
    url = f"https://quotes.toscrape.com/page/{i}/"
    result = requests.get(url)
    q = BeautifulSoup(result.text,"html.parser")
    quote = q.find_all(class_="quote")
    for el in quote:
        text = el.find(class_="text").string[1:-1]
        author = el.find(class_="author").string

        dict[author] = text


with open("data.json","w") as f:
    json.dump(dict,f,indent=4)
