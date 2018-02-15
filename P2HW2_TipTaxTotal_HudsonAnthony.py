# CTI-110 
# P2HW2 - Tip Tax Total 
# Anthony Hudson, Jr.
# 13 FEB. 2018
#

#Price of the meal.
mealTotal = float ( input("What is the price of your meal?"))

#Sales tax.
salesTax = float (.07)

#Gratuity.
gratuity = float (.18)

#Calcucate the amount of tax payed.
mealTax = float (mealTotal * salesTax)

#Calculate the amount of gratuity payed.
gratuityPaid = float (mealTotal * gratuity)

#Calculate the total price of the meal, tax and gratuity.
totalMealcost = (mealTotal * salesTax)+(mealTotal * gratuity) + mealTotal

#Display amount of sales tax applied to bill.
print ("Sales tax:", format (mealTax, ".2f"))

#Display amount of gratuity applied to the bill.
print ("Gratuity:", format (gratuityPaid, ".2f"))

#Display the total cost of the meal.
print ("The cost of you meal is:",totalMealcost)
