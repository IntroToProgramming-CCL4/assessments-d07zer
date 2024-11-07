# EXERCISE 10
# Write a program that tests if a value is even or odd. Follow the instructions outlined below:

# INSTRUCTIONS
# The program should ask the user for a number from within the main function.
# The entered number should be passed to a function that determines if the value is even or odd.
# The function should return a message indicating whether the number is even or odd.
# The message returned by the function should be printed from within the main function.

def oden (nnumser):
    if nnumser % 2 == 0: #The defined function will determine if the given number by checking if it is divisible by 2 without remainder, if so it return the text
        return f"\nThe number {nnumser} is an even number." #stating that it is an even number.
    else: #If the inputted number however has a remainder, it will return the statement that it is an odd number.
        return f"\nThe number {nnumser} is an odd number."

def main(): #The main function is the user prompted to input a number.
    nnumser = int(input("Insert a number: \n"))
    result = oden(nnumser) #Once inputted, the function calls the oden (odd even) function and will print the result
    print (result)         #given by the oden function with the inputted number.

main()