import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests

url = input('Enter URL: ')
count = input('Enter count: ')
count_int = int(count)
index = input('Enter position: ')
final_index = int(index) - 1

# TEST URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(url)

for _ in range(count_int):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    user_tag = tags[final_index]
    clean_tag = user_tag.get('href', None)
