## Automate the whole project.

candidates = input(" Enter the Name of the candidates separated by a space ")
candidates = candidates.split()
#print(type(candidates))


candidate = ""# notice it is a singular candidate ## different variable
while candidate == "":
    candidate = input("Which candidate do you support?\n...")
    if candidate not in candidates:
            print("Please choose the candidates given. Try again.")
            candidate = "" # Reset candidate memory
voters = 0
while voters == 0:
    try:
        voters = int(input(" How many voters are there.? "))
        if voters < 0:
            print("You wrote a negative integer. I have taken the mode value.")
        else:
            pass
    except:
        print('Write an integer value. Please try again.')
        voters = 0

## this 4 line code replaced lines of code. It prevented me from writing multiple loops.
import random
pref = list()
for voter in range(voters):
    pref.append(random.sample(candidates,len(candidates)))# it append the list

## now you receive the list of list of preference of each voter in a sequential order.
#print(' The voter preferences are: ' + str(pref))

## To further split the list of list into a single list
## This is the pattern. create an empty list, then append in it list of list elements in a for loop.
pref_new = []
for tot_pref in pref: ## going through each list within the list. # tot_pref is the variable name for the list within the list.
    for i in range(len(tot_pref)):## going through list elements.
        pref_new.append(tot_pref[i])
#print(pref_new)

seq_list = list()
for seq_ord in range(len(candidates)):
    seq_list.append(pref_new[seq_ord::len(candidates)])## new list of list
#print(seq_list)## list preference wise

## Now you can create a dictionary to count the variables.

list_of_dict_count = []
for count in seq_list:
    dict_count = {}
    for count_elements in count:
        if count_elements not in dict_count:
            dict_count[count_elements]=1
        else:
            dict_count[count_elements] = dict_count[count_elements] + 1
    list_of_dict_count.append(dict_count)## this list of dictionary will have counted preferences of all levels.

print(list_of_dict_count)

final_dict = {}
final_winner = candidates
count_loop = 0
for dic in list_of_dict_count:
    count_loop += 1
    if len(final_winner) == 1:
        print("the final winner: " + str(final_winner[0]))
        break
    lowcount = None
    lowword = ""
    if len(final_dict) == 0: ## this can be for the first time only
        for k,v in dic.items():
            final_dict[k] = v
    else:## from second calculations forward.
        for k, v in dic.items():
            if final_dict[k] == None:
                 pass## the break statement exits the for loop completely
            else:
                final_dict[k] = final_dict[k] + v
    print(final_dict)
        # now final key is updated.
    ## Now to determine candidate with lowest number of votes.
    for k,v in dic.items():
        if final_dict[k] == None:
            pass
        elif lowcount == None or final_dict[k] < lowcount:## this can throw error. prerequired is an updated dict.
             lowcount = final_dict[k]##
             lowword = k
        elif lowcount == final_dict[k]:  # in case if there is more than one lowcounts
            lowword = lowword + " " + k
    low_list = lowword.split()  ## Now you have the candidates with the lowest number of preference at this stage
    ## this loop assign none value to the lowest number in the final list
    for k, v in dic.items():
        if k in low_list:
            print(" At Round " + str(count_loop) + " the eliminated candidate is :" + str(k))
            final_winner.remove(k)
            final_dict[k] = None  ## this will set the valu


print(" the last final dict is " + str(final_dict))
print(" The Winner : " + str(final_winner[0]) + " who cumulatively got " + str(final_dict[final_winner[0]]))
if candidate in final_winner:
    print(" your chosen candidate won ")
else:
    print(" Your Candidate lost")



