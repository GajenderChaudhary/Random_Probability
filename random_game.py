##This game will tell you total number of times your number repeats itself in your decided trials.

try:
    name = str(input(" Namaste! \n In this Program I will tell you How many times your chosen number repeats in the your chosen trials \n What should I call you ? \n Please type your name or press enter to skip \n ___"))
except: ## this exception never throws
    name = " Good Human Being "
    print(" It looks like that you didnt write the name. It's alright! I don't Bite. Okay I will call you  Good Human Being")

#### adding customised range option.

r1 = -50 #range 1
r2 = 50 #range 2
try:
    know_how = int(input(" Namaste " + name + " \n If you wish to know how this random numbers are generated. Please enter 1 or press enter to skip \n ___"))
    if know_how == 1:
        print(" The program ask the user the random number to be put in and then uses that random number and add in it the system generated random number from the default range i.e from minus 50 to 50. \n Each cycle adds a new random number to previous number to get a new random number. ")
        change_the_range = int(input(" if you wish to change the range. please enter 1 or otherwise press enter to skip to proceed with default range. \n ___"))
        if change_the_range == 1:
            r1 = int(input(" Please write an integer value of your first range. \n ___"))
            r2 = int(input(" Please write an integer value of your second range. \n ___"))
        else:
            r1 = -50
            r2 = 50
except:
    pass


try:
    req_trials = int(input(" \n How many trials do you want?\n Please write an integer value keeping in mind the computational power of your computer. \n Or press enter to skip directly to one crore trials \n ___"))
except:
    print(" Proceeding with One crore trials")
    req_trials = 10000000

try:
    req_num = int(input(" \n What number do you want to check in the " + str(req_trials) + " trials ? \n ___"))
except:
    print(" It looks like that you did not write an integer value. \n I am just going to consider zero as your default chosen number. ")
    req_num = 0



try:  ### Try and except block in case user does not put an integer value.
    ran_num = int(input(" \n Write a starting integer number for complete randomness. \n Its just like shuffling. \n I suggest somewhere between minus 50 and 50. \n ___"))
except:
    ran_num = 0
    print(" Please put an integer value next time. \n The computer generated its own random number.")


import random

tot_trial = 0  # iteration variable
tot_zero = 0  ## the number of times zero appeared
pe = 0  ## positively even
ne = 0  ## negatively even
po = 0  ## positively odd
no = 0  ## negatively odd
rn = 0  ## to count required number

while tot_trial < req_trials:
    ran_num = ran_num + random.randint(r1, r2)
    if ran_num % 2 == 0 and ran_num > 0:
        pe = pe + 1
        tot_trial = tot_trial + 1
    if ran_num % 2 == 0 and ran_num < 0:
        ne = ne + 1
        tot_trial = tot_trial + 1
    if ran_num % 2 == 1 and ran_num > 0:
        po = po + 1
        tot_trial = tot_trial + 1
    if ran_num % 2 == 1 and ran_num < 0:
        no = no + 1
        tot_trial = tot_trial + 1
    if ran_num == 0:
        tot_zero = tot_zero + 1
        tot_trial = tot_trial + 1
    if ran_num == req_num:
        rn = rn + 1
        print(" Total trials were " + str(tot_trial))
        print(" Negatively even numbers were " + str(ne))
        print(" Negatively Odd Numbers were " + str(no))
        print(" Positively Even numbers were " + str(pe))
        print(" Positively Odd numbers were " + str(po))
        print(" Total zeroes were " + str(tot_zero))
        print("End of Loop " + str(rn))
    if tot_trial == req_trials:
        print(" Namaste! " + name )
        print(" Your Total Trials reached " + str(tot_zero + no + po + ne + pe))
        print(" Total times You get " + str(req_num) + " in " + str(req_trials) + " trials are " + str(tot_zero))
        print(" Total Negatively Odd Number in " + str(req_trials) + " trials are " + str(no))
        print(" Total Positively Odd Number in " + str(req_trials) + " trials are " + str(po))
        print(" Total Negatively Even Number in " + str(req_trials) + " trials are " + str(ne))
        print(" Total Positively Even Number in " + str(req_trials) + " trials are " + str(pe))
        print(" Total times you get zero were " + str(tot_zero))
        print(" Please rerun program for more trials ")
        print(" Have a nice Day! ")
