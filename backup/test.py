import requests
url = 'https://ru.wikipedia.org/wiki/The_Beatles'
response = requests.get(url)

webpage = response.text 

# print(response.headers)
# print(webpage)

# for key, value in response.headers.items():
#     print(key, ':', value)

# print(response.request.headers)