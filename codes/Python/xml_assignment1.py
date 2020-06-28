import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET
#http://py4e-data.dr-chuck.net/comments_398593.xml is the URL to analyse
#SUM = 2791.0
#ignores SSL Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter URL: ' )
site= urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(site), 'characters')


tree = ET.fromstring(site)
counts = tree.findall('.//count')


sum = 0

for count in counts:

    number= float(count.text)
    sum= sum + number


print(sum)
