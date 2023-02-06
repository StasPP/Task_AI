import requests
from bs4 import BeautifulSoup

url1 = "https://www.google.com/"
url2 = 'https://www.lightinthebox.com/he/p/adults-women-s-cosplay-retro-medieval-dress-cosplay-costume-for-party-halloween-festival-polyster-halloween-carnival-masquerade-dress_p7596584.html?edmdiscountkey=a0010862f59c05f6deab75beeea76391&litb_from=newsletter&user_email=9dc700ce8c89a8fb5604f0b7544129ce9b658929db68d025&crm_features=&mname=he_nl_L20230128_1_M_US128_&p_id=0&c_id=0&send_date=2023012814&utm_source=crm&utm_content=newsletter&utm_medium=newsletter&utm_campaign=LITB20230128US128&content=Product&country_code=US&currency=USD'
response = requests.get(url1)

webpage = response.content

print(webpage)

print(response.headers)

for key, value in response.headers.items():
    print(key, ':', value)
    
print(response.request.headers)

print(response.status_code)