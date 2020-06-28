fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        split=line.split()
        print(split[1])
        count=count+1





print("There were", count, "lines in the file with From as the first word")
