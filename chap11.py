#Search for lines that contain 'From'
import re
fhand = open('mbox.txt')
for line in fhand:
    line.strip()
    if re.search('From:', line):
        print(line)



#Search for lines that start with 'From:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)



#Search for lines that start with 'F', followed by 2 characters
#, followed by 'm:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)



#Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)



#Search for lines that have an @ between characters
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)



#Search for lines that have an @ between characters
#The characters must be a letter or number
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)



#Search for lines that start with "X" followed by any non whitespace
#characters and ':' followed by a space and any number.
#The number can include a decimal
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('X-\S*: [0-9.]+', line):
        print(line)



#Search for lines that start with "X" followed by any non whitespace
#characters and ':' followed by a space and any number.
#The number can include a decimal.
#Then print the number if it is greater than zero.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('X-\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)



#Search for lines that start with 'Details: rev='
#followed by numbers and '.'
#Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)



#Search for lines that start with From and a character
#followed by a two digit number between 00 and 99 followed by ':'
#Then print the number if it is freater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)



# Exercise 1:
import re
hand = open('mbox.txt')
rex = input('Enter a regular expression: ')
counter = 0
for line in hand:
    line = line.rstrip()
    if re.search(rex, line):
        counter += 1
        #print(line)
        #print(counter)

print('mbox.txt had {} lines that matched {}'.format(counter, rex))



#Exercise 2:
import re
fname = input('Enter a file: ')
try:
    hand = open(fname)
except:
    print("Not a valid file name", fname)
    exit()

x = list()
for line in hand:
    line = line.rstrip()
    y = re.findall('N.+ R.+: ([0-9]+)', line)
    if len(y) > 0:
        #print(y)
        x.append(int(y[0]))
        #print(x)
average = sum(x)/len(x)
print("The average number is: ", average)
