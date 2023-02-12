from bs4 import BeautifulSoup
import requests


url ='https://en.wikipedia.org/wiki/Imperial_War_Museum'
# 'https://ru.wikipedia.org/wiki/%D0%98%D0%BC%D0%BF%D0%B5%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BC%D1%83%D0%B7%D0%B5%D0%B9'

soup = BeautifulSoup(requests.get(url).text ,"html.parser")

# stringArr = soup.find_all("div", {"id":"bodyContent"})
stringArr = [p.get_text() for p in soup.find_all("div", {"class":"reflist"}) ] 

# print(stringArr)

# strings = [p.get_text() for p in stringArr]
 
for s in stringArr:
    print(s) 