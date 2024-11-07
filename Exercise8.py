# EXERCISE 8
# Write a program that searches for a specific string within a list of strings. The list is initialized with specific names
# task is to search for "Sam".

lisst = ("hankerchief", "wallace", "gromit", "robotnik", "james", "bob", "sam", "batman") #the list holds the given names

FINDME = input("insert name you are searching for: \n")
name = FINDME.lower() #the variable will set the inputted item into lowercase for convenience

if name in lisst: #will actively search the list for the item described by the input
    print (f"\nThe name, {FINDME}, is in the list. ")
    
else: #if not, it will return this message.
    print (f"\nThe name, {FINDME} is not available.")
