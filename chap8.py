#Exercise 1:
def chop(t):
    t.pop(0); t.pop()
    return None

def middle(t):
    return t[1:len(t)-1]

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 8, 9]

c = chop(a)

d = middle(b)
print(c, a)
print(d, b)



#Exercise 2:
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or len(words) < 3 : continue
    if words[0] != 'From' : continue
    print(words[2])


#Exercise 3:
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if (len(words) == 0 or len(words) < 3) and words[0] != 'From':
        continue
    print(words[2])



# Exercise 4:
fhand = open('romeo.txt')
wordlist = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word in wordlist: continue
        wordlist.append(word)
wordlist.sort()
print(wordlist)



# Exercise 5:
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From') and not line.startswith('From: '):
        count += 1
        words = line.split()
        print(words[1])
print('There were {} lines in the file with From as the first word'.format(count))



#Exercise 6:
numlist = list()
maximum = None
minimum = None

while True:
    try:
        n = input("Enter a number: ")
        if n == 'done' or len(n) < 1:
            break
        else:
            number = float(n)

    except:
        print("Invalid input")
        continue
    numlist.append(number)

maximum = max(numlist)
minimum = min(numlist)

print("Maximum: {}\nMinimum: {}".format(maximum, minimum))
