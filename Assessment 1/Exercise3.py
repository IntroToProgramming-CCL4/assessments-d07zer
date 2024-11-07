# EXERCISE 3
# Store the information (name, hometown, and age) as key-value pairs in a dictionary.

Print the values on separate lines using a single print() statement.
Use variables with appropriate data types for each piece of information.
# This declares a dictionary, each states the key and value of the following.
informacion = {'name: ':'Schaftenheinshmert', 'hometown: ':'Dusseldorf', 'age: ':'957'}
for key, value in informacion.items(): # Extracts the keys and values
    print (key, value)

#ADVANCED
# Have the user input their name, hometown, and age instead of hardcoding the values.

guyfo = {'name':'N\A', 'last name':'N\A', 'hometown':'N\A', 'age':'N\A'} #the dictionary items are defaulted as N\A.

an = input("\nView dictionary or Proceed (Proceed/View): \n") #this will simply ask the user whether they require to view the dictionary or proceed before adding in the values.
ans = an.lower() #converts the inputs into lowercase for convenience.
if ans == "proceed": #if command is inputted with "proceed" then it will proceed with the questions to fill the list.
    nam, lastnam = input("\nWhat is your Name (First/Last): \n").split() #to accompany both first and last name, both name and lastname variables are declared.
    guyfo['name'] = nam
    guyfo['last name'] = lastnam #the given input will be added to the list in the respective keys.
    hom = input("\nWhat is your Hometown: \n")
    guyfo['hometown'] = hom
    agg = int(input("\nWhat is your Age: \n"))
    guyfo['age'] = agg
    for key, value in guyfo.items(): # Extracts the keys and values
        print (key, value)
elif ans == "view": #inputting "view" will simply redirect to this.
    for key, value in guyfo.items(): # Extracts the keys and values
        print (key, value)
else: #failsafe measure so that it can strictly take in "proceed" or "view" as inputs, otherwise it will display this
    print ("Invalid input")