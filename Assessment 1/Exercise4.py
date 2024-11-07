# EXERCISE 4
# In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

# STEPS
# Write a program that asks the user "What is the capital of France?" and waits for their response.
# If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
# If the answer is incorrect, the program should print a message saying the answer is wrong.

# ADVANCED
# Ignore Capitalization
# 10 Questions of each european capitals

print ("Welcome to THE quiz") #introductory text displayed on the top, purely cosmetic

score = 0 #this is the initial score count at the beginning

print ('\n\tQUESTION 1') #purely cosmetic, and states the question number to keep the use in track.
corans = input("\nWhat is the capital of France? \n")
ans = corans.lower() #the given input here in this declared variable will be lowercased
                     #this will allow the inputted answer (if correct) to be accapted by the regardless of placements of upper/lowercase.
if ans == "paris":
    score = score + 1 #adds a value to the user score if the answer is correct
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.") #will display the current score standings upon completion of a question.
    
else:
    score = score - 1 #if the answer is incorrect, the program deducts the score.
    print ("Incorrect. The Capital of France is Paris.")
    print ("-1 Points")
    print (f"your score is currently {score}.")
                                                  #the whole sequence of the first question repeats
print ('\n\tQUESTION 2')
corans = input("\nWhat is the capital of Sweden? \n")
ans = corans.lower()

if ans == "stockholm":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of Sweden is Stockholm.")
    print ("-1 Points")
    print (f"your score is currently {score}.")

print ('\n\tQUESTION 3')
corans = input("\nWhat is the capital of Russia? \n")
ans = corans.lower()

if ans == "moscow":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of Russia is Moscow.")
    print ("-1 Points")
    print (f"your score is currently {score}.")
    
print ('\n\tQUESTION 4')
corans = input("\nWhat is the capital of Denmark? \n")
ans = corans.lower()

if ans == "copenhagen":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of Denmark is Copenhagen.")
    print ("-1 Points")
    print (f"your score is currently {score}.")

print ('\n\tQUESTION 5')
corans = input("\nWhat is the capital of Moldova? \n")
ans = corans.lower()

if ans == "chisinau":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of Moldova is Chisinau.")
    print ("-1 Points")
    print (f"your score is currently {score}.")

print ('\n\tQUESTION 6')
corans = input("\nWhat is the capital of Slovenia? \n")
ans = corans.lower()

if ans == "ljubljana":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of Slovenia is Ljubljana.")
    print ("-1 Points")
    print (f"your score is currently {score}.")
    
print ('\n\tQUESTION 7')
corans = input("\nWhat is the capital of Cyprus? \n")
ans = corans.lower()

if ans == "nicosia":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of Cyprus is Nicosia.")
    print ("-1 Points")
    print (f"your score is currently {score}.")

print ('\n\tQUESTION 8')
corans = input("\nWhat is the capital of North Macedonia? \n")
ans = corans.lower()

if ans == "skopje":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of North Macedonia is Skopje.")
    print ("-1 Points")
    print (f"your score is currently {score}.")

print ('\n\tQUESTION 9')
corans = input("\nWhat is the capital of Malta? \n")
ans = corans.lower()

if ans == "valletta":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of Malta is Valletta.")
    print ("-1 Points")
    print (f"your score is currently {score}.")

print ('\n\tQUESTION 10')
corans = input("\nWhat is the capital of San Marino? \n")
ans = corans.lower()

if ans == "san marino":
    score = score + 1
    print ("Correct!")
    print (f"You have gained 1 point, your score is currently {score}.")
    
else:
    score = score - 1
    print ("Incorrect. The Capital of San Marino is... San Marino.")
    print ("-1 Points")
    print (f"your score is currently {score}.")

print (f"\nYour final score is {score}.")
if score < 0:
    print ("\nHow?")

elif score == 0:
    print ("\nIm more impressed you have consistently held up this score level the entire quiz.")
    
elif score == 5:
    print ("\nYou've done alright, but do better.")

elif score >= 6:
    print ("\nYou're doing fantaaaaaastic!")
    
elif score == 10:
    print ("\nYou have ACED this, You are a VERY knowledgable person.")
    # these are results that would be displayed depending on the amount the user has scored.
 