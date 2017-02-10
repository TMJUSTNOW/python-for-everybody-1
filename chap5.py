#Exercise 1:
total = 0
count = 0
average = 0

while True:
    try:
        n = input("Enter a number: ")
        if n == "done" or len(n) < 1: #if the user just press enter
            break
        else:
            number = float(n)
    except:
        print("Invalid input")
        continue
    total = total + number
    count = count + 1
    average = total / count

print("{} {} {}".format(total, count, average))



#Exercise 2:
maximum = None
minimum = None

while True:
    try:
        n = input("Enter a number: ")
        if n == "done" or len(n) < 1:
            break
        else:
            number = float(n)
    except:
        print("Invalid input")
        continue
    if maximum == None or number > maximum:
        maximum = number
    if minimum == None or number < minimum:
        minimum = number

print("The max is: {}. The min is: {}".format(maximum, minimum))
