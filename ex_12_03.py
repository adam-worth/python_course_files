from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

lst = list()
count = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('test_url: http://py4e-data.dr-chuck.net/known_by_Fikret.html')
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# user_count = input('Enter count: ')
# user_position = input('Enter position: ')
tags = soup('a')
for tag in tags:
    tag = tag.decode().rstrip()
    names = re.findall('(?<=\>)(.*?)(?=\<)', tag)
    # for name in names:
    #     print(name)
