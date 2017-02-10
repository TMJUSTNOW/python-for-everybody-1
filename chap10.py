# #Count top ten of romeo
# import string
# fhand = open('romeo-full.txt')
# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# #Sort the dictionary by value
# lst = list()
#
# for key, val in list(counts.items()):
#     lst.append((val, key))
#
# lst.sort(reverse=True)
#
# for key, val in lst[:10]:
#     print(key, val)
#
# print(lst)
# print(counts)
#
#
#
# #Exercise 1:
# fname = input("Enter a file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("File cannot be opened", fname)
#     exit()
#
# mail = dict()
# for line in fhand:
#     if not line.startswith("From"): continue
#     if line.startswith("From: "): continue
#     words = line.split()
#     mail[words[1]] = mail.get(words[1], 0) + 1
#
# lst = list()
# for key, val in list(mail.items()):
#     lst.append((val, key))
#
# lst.sort(reverse=True)
#
# for key, val in lst[:1]:
#     print(val, key)
#
#
#
# #Exercise 2:
# fname = input("Enter a file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("File cannot be opened", fname)
#     exit()
#
# hours = dict()
# for line in fhand:
#     if not line.startswith('From'): continue
#     if line.startswith("From: "): continue
#     words = line.split()
#     hour, minutes, seconds = words[5].split(':')
#     hours[hour] = hours.get(hour, 0) + 1
# print(hours)
#
# hlst = list()
# for key, val in list(hours.items()):
#     hlst.append((key, val))
#
# hlst.sort(reverse = False)f
#
# for key, val in hlst:
#     print(key, val)
#
#
#
# Exercise 3:
import string
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened", fname)
    exit()

counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', '0,1,2,3,4,5,6,7,8,9'))
    line = line.lower()
    words = line.split()
    delimiter = ''
    letters = delimiter.join(words)
    for ltr in letters:
        counts[ltr] = counts.get(ltr, 0) + 1
print(counts)

letter_list = list()

for key, val in list(counts.items()):
    letter_list.append((val, key))

letter_list.sort(reverse=True)

for key, val in letter_list:
    print(val, key)



#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# #Sort the dictionary by value
# lst = list()
#
# for key, val in list(counts.items()):
#     lst.append((val, key))
#
# lst.sort(reverse=True)
#
# for key, val in lst[:10]:
#     print(key, val)
#
# print(lst)
# print(counts)
