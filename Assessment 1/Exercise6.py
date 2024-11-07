# EXERCISE 6
# Write a program that simulates a password entry system.
# The correct password is defined as 12345.
# The program should keep asking the user to enter the password until they provide the correct one.

# Basic Requirements:
# Define the correct password.
# Use a while loop to repeatedly ask the user for the password until the correct one is entered.
# Output an appropriate message when the correct password is entered.

print ("Welcome to [][][][][][][][][] Inc.!") #cosmetic

correctpass = 12345 #this variable holds the correct passkey.
corpas = str(correctpass) #this variable simply converts the previous variable into a string to ensure convenience incase there is a change in passkey.

attempts = 0 #this variable holds the attempt counter, each wrong input in the password increases the value.

while attempts < 5: #this allows the user to attempt inputting the password 5 times until the maximum limit has reached.
    passwor = input("\nEnter Password: \n")
    if passwor == corpas: #if the correct password has been inputted, it will proceed with this line and breaks the loop.
        print ("\nAccess Granted! Welcome, User.")
        break
    else: #each wrong attempt leads to this, and will add one value to the attempt counter until the set maximum has been reached.
        print ("\nAccess Denied.")
        attempts += 1
# OPTIONAL PART (max 5 attempts)

if attempts == 5: #once the maximum amount of attempts is reached, it will then proceed to this line.
    print ("\nYou have reached the maximum number of attempts. \nThe authorities have been alerted.")