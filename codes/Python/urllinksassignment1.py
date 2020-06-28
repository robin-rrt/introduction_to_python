import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
site = urlopen(url, context=ctx).read()
soup = BeautifulSoup(site, "html.parser")

sum=0
tags = soup('span')
for tag in tags:

    number=float(tag.contents[0])
    sum=sum+number
print(sum)
