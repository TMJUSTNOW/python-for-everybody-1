#Exercise 1
import random

for i in range(10):
    x = random.random()
    print(x)


Exercise 2:
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()



#Exercise 3:
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()



Exercise 4:
Option B: It is the beginning of the function



Exercise 5:
Option D: ABC Zap ABC


Exercise 6:
factor = 1.5 #increment factor after 40 hours
hlimit = 40 #hours for increment
def computepay():
    try:
        hours = float(input("Enter hours: "))
        rate = float(input("Enter rate: "))
        if hours <= hlimit:
            pay = round(hours * rate, 2)
        else:
            overh = hours - hlimit
            pay = round((hlimit * rate) + (overh * rate * factor), 2)
        print("Pay: {}".format(pay))
        return pay
    except:
        print("Error, please enter a numerix input for rate")

computepay()



#Exercise 7:
def computegrade():
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

computegrade()
