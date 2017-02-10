name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

senders=list()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if words == [] : continue
    if words[0] != "From" : continue
    senders.append(words[1])

count = dict ()

for word in senders:
	count[word] = count.get(word,0) + 1

bigcount = None
bigword = None

for word, count in  count.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount