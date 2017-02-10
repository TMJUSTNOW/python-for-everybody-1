#Assignment code:
import re
fname = input('Enter a file: ')
try:
    hand = open(fname)
except:
    print("Not a valid file name", fname)
    exit()

count = 0
total = 0
for line in hand:
    line = line.rstrip()
    y = re.findall('([0-9]+)', line) #find numbers
    if len(y) > 0:  #if there are numbers in the line...
        # print(line)
        # print(y)
        count = count + len(y)
        for num in range(len(y)): #iterate on the list y
            y[num] = int(y[num])
            total = total + y[num]
print("The sum of all numbers is: ", total, count)
