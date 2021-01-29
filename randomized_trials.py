## same as previous random game but with more efficient code.

name = str(input(" Hi! I am Garry, your assistant. What would you like me to call you! \n ..."))
if name == "":
    print(" Ok then, I thought we were friends. Anyways I will just call you Friend")
    name = "Friend"
else:
    pass

print(" Hello " + name + "! This program will let you carry out random trials. Please enjoy.")

try:## remember that whenever you have an integer input there are always chances that your code can throw error.
    know_how = int(input(" if you wish to know the algorithm behind the scenes, enter 1 or otherwise press enter to skip \n ..."))
    if know_how == 1:
        print(" The computer will generate random numbers based on the built in random module of python.")
    else:
        pass
except:
    pass

req_trials = 0
while req_trials <= 0:
    try:
        req_trials = int(input(" How many trials do you want me to do. please write an integer value keeping in mind computational power of your CPU.\n ..."))
        if req_trials < 0:
            req_trials = req_trials * -1
            print(" It looks like that you wrote a negative number. I am going to make it positive. \n Now we will be carrying out" + req_trials + "trial/s.")
        else:
            pass
    except:
        except1 = input(" It looks like that you didn't write an integer value. \n Press enter to try again, or otherwise you can type what i call you to proceed with the default one crore trials. ")
        if except1 == name:
            req_trials = 10000000
        else:
            pass
req_num = ""
while req_num == "":## this was more innovative way to enter this loop.
    try:
        req_num = int(input(" What integer do you want to check in the trials.? \n ..."))
    except:
        print("It looks like you didn't write an integer value. \n Try again...")


r1 = ""
r2 = ""

while r1 == "":
    try:
        r1 = int(input(" \n What is range within which you want to check your number? \n write your first range.\n ..."))
    except:
        print(" Please write an integer value. Try again!")

while r2 == "":
    try:
        r2 = int(input(" write the second range.\n ..."))
    except:
        print(" Please write an integer value. Try again!")

print(" OK! so let me summarize. \n The number you want to check is " + str(req_num) + ".")
print(" The number of trial/s you want me to carry out is/are " + str(req_trials) + ".")
print(" Your First range is " + str(r1) + ".")
print(" Your second range is " + str(r2) + ".")

import random
tot_trials = 0
count_req_num = 0

while tot_trials < req_trials:
    tot_trials +=1
    ran_num = random.randint(r1,r2)
    if ran_num == req_num:
        count_req_num +=1

print(" So " + name + "!, This is the result of the trial/s \n ")
print(str(count_req_num) + " times you get the number " + str(req_num) + " in " + str(req_trials) + " trials." )



