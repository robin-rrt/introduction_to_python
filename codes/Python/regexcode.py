fname= input('Enter File Name:')
fhand=open(fname)
sum=0
import re
for line in fhand:
    line=line.rstrip()
    numbers= re.findall('[0-9]+' , line)
    for number in numbers:
        x=float(number)
        sum=sum+x
print (sum)
