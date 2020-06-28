# Use words.txt as the file name
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count=count+1
    pos=line.find(':')
    num=float(line[pos+1:])
    tot=num+tot

avg=tot/count
print('Average spam confidence:',avg)
