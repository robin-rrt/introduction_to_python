fname=input('Enter file name:')
if len(fname)<1 :
    fname='mbox-short.txt'
fh = open(fname)

count=0
for line in fh:
    count= count+1

print('Number of lines in this file:',count)
