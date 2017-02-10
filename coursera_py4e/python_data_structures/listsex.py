fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if words == [] : continue
    if words[0] != "From" : continue
    print '=====ss==', words[2]