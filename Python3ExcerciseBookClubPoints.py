# CTI-110
# Python 3 Excercise, Book Club Points
# Anthony Hudson, Jr.
# 1 MAR. 2018
#

#Obtain number of books purchased.
booksPurchased = int(input("How many books have you purchased this month? "))

#Decisions based on user input.
if booksPurchased <= 1:
    print ("You have not earned points")
elif booksPurchased == 2 or booksPurchased == 3:
    print ("You have earned 5 points")
elif booksPurchased == 4 or booksPurchased == 5:
    print ("You have earned 15 points")
elif booksPurchased == 6 or booksPurchased == 7:
    print ("You have earned 30 points")
elif booksPurchased >= 8 or booksPurchased == 9:
    print ("You have earned 60 points")
