#Exercise 2:
name = input("Enter your name: ")
print("Hello {}".format(name))

#Exercise 3:
hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = round(hours * rate, 2)
print("Pay: {}".format(pay))

#Exercise 4:
width = 17
height = 12.0

print(width//2)
print(type(width//2))
print(width/2.0)
print(type(width/2.0))
print(height/3)
print(type(height/3))
print(1 + 2 * 5)
print(type(1 + 2 * 5))

#Exercise 5:
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = 9 / 5 * celsius + 32
print("The temperature in fahrenheit is {}".format(fahrenheit))
