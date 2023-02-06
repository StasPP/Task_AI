import requests
from bs4 import BeautifulSoup
url1 = 'https://ru.wikipedia.org/wiki/The_Beatles'
# url1 = 'https://shubhamsayon.github.io/python/demo_html.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

response = requests.get(url1, headers=headers)

webpage = response.content

print(response.status_code)

# create BeautifulSoup object (we could use different parsers)
soup = BeautifulSoup(webpage,"html.parser")

# print(soup)

# print(soup.p.prettify())

# print(soup.head.contents)

for string in soup.body.strings:
    print(string) 

# for child in soup.body.children:
#     if (child != '\n'):
#         print(child.name)
