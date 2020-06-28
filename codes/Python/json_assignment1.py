import json
import urllib.request, urllib.parse, urllib.error
import ssl


#ignores SSL Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#takes url and opens it and reads it.
url= input('Enter URL: ' )
site= urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(site), 'characters')

info = json.loads(site)
print('User count:', len(info))

sum = 0
count = 0
#you have to loop through comments, if you loop through the 'info' json directly, the first line will cause errors
for item in info['comments']:
    x = float(item['count'])
    sum = sum + x
    count = count + 1
print('COUNT', count)
print(sum)
#http://py4e-data.dr-chuck.net/comments_398594.json
# SUM = 2606.0
