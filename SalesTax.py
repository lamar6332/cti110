# CTI-110 
# Python 2 Excercise
# Anthony Hudson, Jr.
# 20 FEB. 2018
#

#Amount of purchase.
purchase = float ( input("What is the amount of your purchase? "))

#State tax.
stateTax = .025

#Sales tax.
countyTax = .05

#Calculation, total sales tax.
total = (stateTax * purchase)+(countyTax * purchase) + purchase

#Calcualte with state tax.
stateTax1 = stateTax * purchase

#Calcualte with county tax.
countyTax1 = countyTax * purchase

#Display county tax.
print ("County tax:", format (countyTax1, ".2f"))

#Display state tax.
print ("State tax:", format (stateTax1, ".2f"))

#Display total cost with taxes.
print ("Total:", format (total, ".2f"))
