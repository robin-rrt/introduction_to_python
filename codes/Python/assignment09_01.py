fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
sender = list()
dict=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        split=line.split()
        dict[split[1]]=dict.get(split[1],0) + 1

bigcount = None
bigname = None
for name,count in dict.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigname = name

print(bigname,bigcount)
