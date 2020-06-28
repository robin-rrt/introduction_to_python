fname=input('Enter file name:')
if len(fname)<1 :
    fname='mbox-short.txt'

counts=dict()
fhand=open(fname)
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        words=line.split()
        date= words[5]
        days=date.split(':')
        counts[days[0]] = counts.get(days[0],0) + 1

print(sorted([(key,val) for key,val in counts.items()]))
print('or')
for key,val in sorted(counts.items()):
    print(key,val)
