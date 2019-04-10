import requests
from bs4 import BeautifulSoup
url=("www.amazon.in")
code=requests.get("https://"+url)
plain=code.text
soup=BeautifulSoup(plain,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
