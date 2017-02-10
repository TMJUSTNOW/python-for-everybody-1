#Exercise 1:
factor = 1.5 #increment factor after 40 hours
hlimit = 40 #hours for increment
hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

if hours <= hlimit:
    pay = round(hours * rate, 2)
else:
    overh = hours - hlimit
    pay = round((hlimit * rate) + (overh * rate * factor), 2)
print("Pay: {}".format(pay))



#Exercise 2:
factor = 1.5 #increment factor after 40 hours
hlimit = 40 #hours for increment

try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    if hours <= hlimit:
        pay = round(hours * rate, 2)
    else:
        overh = hours - hlimit
        pay = round((hlimit * rate) + (overh * rate * factor), 2)
    print("Pay: {}".format(pay))
except:
    print("Error, please enter a numerix input for rate")



#Exercise 3:
try:
    score = float(input("Enter score: "))

    if score <= 1.0 and score >= 0.0 and score >= 0.9:
        print("A")
    elif score <= 1.0 and score >= 0.0 and score >= 0.8:
        print("B")
    elif score <= 1.0 and score >= 0.0 and score >= 0.7:
        print("C")
    elif score <= 1.0 and score >= 0.0 and score >= 0.6:
        print("D")
    elif score <= 1.0 and score >= 0.0 and score < 0.6:
        print("F")
    else:
        print("Bad score")

except:
    print("Bad score - SCORE")
