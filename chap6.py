#Exercise 1
#with while
index = -1
while len("caramelo") > abs(index) - 1:
    print("caramelo"[index])
    index += -1

#with for
strtest = "caramelo"
for char in strtest:
    print(strtest[])



#Exercise 2
#prints the whole string



#Exercise 3:
def word_count(word, let_count):
    count = 0
    for letter in word:
        if letter == let_count:
            count = count + 1
    print(count)

word_count("otorrinolaringologo", "o")



#Exercise 4:
'banana'.count('a')



#Exercise 5:
str = 'X-DSPAM-Confidence:0.8475'

dotpos = str.find('.')
decimal = str[dotpos + 1:]
floatdec = float(decimal)

print(floatdec)
