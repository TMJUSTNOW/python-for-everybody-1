#7.2 Write a program that prompts for a file name, then opens
# that file and reads through the file, looking for lines of
# the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from
# each of the lines and compute the average of those values
# and produce an output as shown below.
#You can download the sample data at
# http://www.pythonlearn.com/code/mbox-short.txt when you are
# testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
decvalue=0
posdecvalue=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
    	continue
    count=count+1
    line=line.rstrip()
    posdecvalue=line.find("0")
    decvalue=decvalue+int(line[posdecvalue+2:])
    #print (line)
    #print (decvalue)

#print (decvalue)
#print (count)

asc=(float(decvalue)/float(count))
strasc=str(asc)
#print (asc)
#print (strasc)

ent=str(int(asc))
#print (ent)
#print (len(ent))

dec=strasc[len(ent)+1:len(strasc)]
#print(dec)
#print(len(strasc))

print ("Average spam confidence: 0."+ent+dec)