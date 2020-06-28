fname=input('Enter File name:')
try:
    fhand=open(fname)
except:
    print('Error,File not found')
    quit()
list=list()
for line in fhand:
    line=line.rstrip()
    words=line.split()
    for element in words:
        if element in list:
            continue
        else:
            list.append(element)

list.sort()
print(list)


    
