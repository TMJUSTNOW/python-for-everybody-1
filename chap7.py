#Exercise 1:
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print("Enter a proper name. {} does not exist.".format(fname))
    exit()
for line in fhand:
    line = line.upper().rstrip() #format the lines in upper and remove spaces
    print(line)


#Exercise 2:
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print("Enter a proper name. {} does not exist.".format(fname))
    exit()
totspam = 0
totlinesspam = 0

for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    totspam += float(line[line.find("0"):])
    totlinesspam += 1

avgspam = totspam/totlinesspam
print("Average spam confidence: {}".format(avgspam))



#Exercise 3:

fname = input('Enter the file name: ')
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
