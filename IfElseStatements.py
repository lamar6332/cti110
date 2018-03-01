# CTI-110 
# Python Excercise, If/Else Statements
# Anthony Hudson, Jr.
# 22 FEB. 2018
#

#Hours worked.
hours_worked = int(input("How many hours have you worked? "))

#Hourly rate.
hourly_rate = 10

#Calculations
reg_pay = hourly_rate * 40
ov_hours = hours_worked - 40
ov_pay = (ov_hours * hourly_rate) * 1.5



if hours_worked > 40:
    gross_pay = reg_pay + ov_pay
    print ("This is what you've earned including overtime: ",gross_pay)

else:
    gross_pay = hours_worked * hourly_rate
    print ("No overtime. This is what you've earned: ",gross_pay)

