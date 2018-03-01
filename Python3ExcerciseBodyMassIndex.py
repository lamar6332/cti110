# CTI-110
# Python 3 Excercise, Body Mass Index
# Anthony Hudson, Jr.
# 1 MAR. 2018
#

#Obtain interger values from user.
weight = int(input("How much do you currently weigh? "))
height = float(input("How tall are you in inches? "))

#Calculatuions based on user input.
bmi = weight * 703 / (height * height)

#Display BMI.
print ("BMI is: ", format (bmi,".2f"))

#Decisions based on user input and calculations.
if bmi >= 18.5 and bmi <= 25:
    print ("You are at your optimal weight.")
elif bmi < 18.5:
    print ("You are underweight.")
elif bmi > 25:
    print ("You are overweight.")
