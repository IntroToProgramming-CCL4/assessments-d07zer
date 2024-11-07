# EXERCISE 5
# Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

#Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#Input Handling: Ask the user to input the month number.
#Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

#These are declared variables of a specific month with it's day counter
ja = 31 # JANUARY
fe = 28 # FEBRUARY
ma = 31 # MARCH
ap = 30 # APRIL
my = 31 # MAY
jn = 30 # JUNE
jy = 31 # JULY
au = 31 # AUGUST
se = 30 # SEPTEMBER
oc = 31 # OCTOBER
no = 30 # NOVEMBER
de = 31 # DECEMBER


mont = int(input("Enter the Month Number (1-12): \n")) #asks for input on month number.
# 1 is January, 2 is February, 3 is March, 4 is April, 5 is May, 6 is June.
# 7 is July, 8 is August, 9 is September, 10 is October, 11 is November, 12 is December.

if mont == 1:
    print (f"\n\tJanuary has {ja} Days,", ja*24,"Hours,", ja*1440, "Seconds in a year.") # In each of the programs displaying the month, there is a
                                                                                         # counter that not only specifies the amount of days,
# ADVANCED                                                                               # but will specifically include the total hours and seconds in that month.
# Leap Year Adjustment
elif mont == 2:                                                                          
    yr = int(input("Insert year number: \n"))                                            
    if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0: # If the given value is divisible by 4, and not by 100 or exactly divisible by 400, then it is a leap year.
        print (f"\n{yr} is a Leap Year.")
        print ("\n\tFebruary has 29 Days,", 29*24, "Hours,", 29*1440, "Seconds in a Leap year.")
    else:
        print (f"{yr} is a Normal Year.") # If the given value is not of the requirements, then it defaults to 28 days.
        print (f"\n\tFebruary has {fe} Days,", fe*24,"Hours,", fe*1440, "Seconds in a year.")
elif mont == 3:
    print (f"\n\tMarch has {ma} Days,", ma*24,"Hours,", ma*1440, "Seconds in a year.")
elif mont == 4:
    print (f"\n\tApril has {ap} Days,", ap*24,"Hours,", ap*1440, "Seconds in a year.")
elif mont == 5:
    print (f"\n\tMay has {my} Days,", my*24,"Hours,", my*1440, "Seconds in a year.")
elif mont == 6:
    print (f"\n\tJune has {jn} Days,", jn*24,"Hours,", jn*1440, "Seconds in a year.")
elif mont == 7:
    print (f"\n\tJuly has {jy} Days,", jy*24,"Hours,", jy*1440, "Seconds in a year.")
elif mont == 8:
    print (f"\n\tAugust has {au} Days,", au*24,"Hours,", au*1440, "Seconds in a year.")
elif mont == 9:
    print (f"\n\tSeptember has {se} Days,", se*24,"Hours,", se*1440, "Seconds in a year.")
elif mont == 10:
    print (f"\n\tOctober has {oc} Days,", oc*24,"Hours,", oc*1440, "Seconds in a year.")
elif mont == 11:
    print (f"\n\tNovember has {no} Days,", no*24,"Hours,", no*1440, "Seconds in a year.")
elif mont == 12:
    print (f"\n\tDecember has {de} Days,", de*24,"Hours,", de*1440, "Seconds in a year.")
else:
    print ("That is an invalid number.") #If the number inputted is not a value between 1-12, it will display this text.
