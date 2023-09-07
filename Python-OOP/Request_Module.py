# Need to install request module first

import requests

# response = requests.get("https://www.codewithharry.com")
# print(response.text)


url = "https://www.codewithharry.com/blog"

r = requests.get(url)

# print(r.text)

# bs4 module for scrapping parsing html

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text,'html.parser')

# print(soup.prettify())

for heading in soup.findAll("p"):
    print(heading.text)
