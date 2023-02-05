url = 'https://ru.wikipedia.org/wiki/The_Beatles'
print(url)

import requests
r = requests.get(url) 
html = r.text

# f = open('test.html', 'w')
# f.write(html)
# f.close()

print(html)