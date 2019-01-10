import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import itertools

count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


for tag in tags:
    clean_link = tag.get('href', None)
    initial_link = clean_link[nt]
    print(initial_link)
    # for i in range(set_run_threshold):
    #     if count == set_run_threshold: break
    #     else: continue
    #     html = urllib.request.urlopen(first_tag_wanted, context=ctx).read()
    #     soup = BeautifulSoup(html, 'html.parser')
    #     count = count + 1






    # for tag in tags:
    #     open_again = urllib.request.urlopen(first_tag_wanted, context=ctx).read()
    #     soup = BeautifulSoup(open_again, 'html.parser')

# for tag in tags:
#     tag = tag.get('href', None).split()
#     for urls in tag:
#         lst.append(urls)
#         count = count + 1
#         url_to_follow = lst[nt]
# print('Retrieving:', lst[nt])

    # for item in itertools.islice(lst, None, None, nt):
    #     print(item)
    # for index, item in enumerate(list):
    #     if index % cownt == 0:
    #         print(list[::4])
    #     print(index, item)
