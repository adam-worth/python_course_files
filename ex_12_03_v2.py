# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = 0
global_url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('test_url: http://py4e-data.dr-chuck.net/known_by_Fikret.html')
url = input('Enter URL: ')
c = input('Enter count:')
cownt = int(c)
set_run_threshold = cownt - 1
n = input('Enter position:')
nt = int(n) - 1

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
user_tag = tags[nt]
first_tag_wanted = user_tag.get('href', None)
# print('Recieving: ', first_tag_wanted)

html2 = urllib.request.urlopen(first_tag_wanted, context=ctx).read()
soup = BeautifulSoup(html2, 'html.parser')

# Retrieve all of the anchor tags
second_tags = soup('a')
unser_tag2 = second_tags[nt]
second_tag_wanted = unser_tag2.get('href', None)
# print('Recieving: ', second_tag_wanted)


def parse_web_page_and_clean_urls():
    html2 = urllib.request.urlopen(global_url, context=ctx).read()
    soup = BeautifulSoup(html2, 'html.parser')

    # Retrieve all of the anchor tags
    second_tags = soup('a')
    unser_tag2 = second_tags[nt]
    clean_second_tag = unser_tag2.get('href', None)
    print('Recieving: ', clean_second_tag)
    return clean_second_tag


for i in range(5):
    global global_url
    global_url = parse_web_page_and_clean_urls()
    print(global_url)
