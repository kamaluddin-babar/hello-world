# finding word which is present maximum in a file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
counts = dict()
names = list()
for line in fhand :
    line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
    #for word in words :
    counts[words[1]] = counts.get(words[1], 0) + 1
#print(counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword, bigcount)

# This is an extra comment to see how git work.
