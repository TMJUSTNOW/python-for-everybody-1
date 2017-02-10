#Exercise 1:
#Way 1
fhand = open('words.txt')
words_dict = dict()
vals = 0

for line in fhand:
    words = line.split()
    for word in words:
        words_dict[word] = vals
        vals += 1

print("Is in dictionary: ", 'is' in words_dict)
print("And in dictionary: ", 'and' in words_dict)
print("Political in dictionary: ", 'political' in words_dict)


Way 2
newdict = dict()
count = 0
fhand = open('words.txt')

inp = fhand.read()
inp = inp.split()

for word in inp:
    count += 1
    newdict[word] = count

print("Is in dictionary: ", 'is' in newdict)
print("And in dictionary: ", 'and' in newdict)
print("Political in dictionary: ", 'political' in newdict)



# Text file histogram (only text):
#         Opening the file
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened: {}'.format(fname))
    exit()
#           Extracting the words
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#print(counts)

#           to order the list
word_list = list(counts.keys())
word_list.sort()
for key in word_list:
    print(key, counts[key])



#Text file histogram# (including punctuation):
#           Get libraries, open file
import string
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fhand)
    exit()

#           extracting the words
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#           to order the list
word_list = list(counts.keys())
word_list.sort()
for key in word_list:
    print(key, counts[key])



Exercise 2:
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    exit()

days = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        dayofweek = words[2]
        days[dayofweek] = days.get(dayofweek, 0) + 1
print(days)



Exercise 3:
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened", fname)
    exit()

mail = dict()
for line in fhand:
    if not line.startswith("From: "): continue
    words = line.split()
    mail[words[1]] = mail.get(words[1], 0) + 1
print(mail)



#Exercise 4:
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened", fname)
    exit()

mail = dict()
for line in fhand:
    if not line.startswith("From: "): continue
    words = line.split()
    mail[words[1]] = mail.get(words[1], 0) + 1
#print(mail)

namelargest = ''
largest = None
for key in mail:
    if largest is None or mail[key] > largest:
        largest = mail[key]
        namelargest = str(key)
print(namelargest, largest)



#Exercise 5:
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File {}.txt cannot be opened".format(fname))
    exit()

domain_name = dict()
for line in fhand:
    if not line.startswith("From: "): continue
    words = line.split()
    linedomain = words[1].split("@")[1] #first word and separate based on @
    domain_name[linedomain] = domain_name.get(linedomain, 0) + 1
print(domain_name)
