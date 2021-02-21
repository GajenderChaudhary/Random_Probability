## Biases embedded in data based probability calculations.
## Draw a sample from the population and then check for changing probability at each simulation.
## at first draw, each unit of population has 1/population chance of being picked. But that is crude understanding.
# conditional probability works in a different sense.


Population = 0
while Population == 0:
    try:
        Population = int(input(" What is the population size ? "))
    except:
        Population = 0
        print(" write an integer value ")

sample = 0
while sample == 0:
    try:
        sample = int(input( " what is the sample size"))
    except:
        sample = 0
        print(" try again ")

# feeding data
simulations = 0
while simulations == 0:
    try:
        simulations = int(input( " How many simulations do you want to run "))
    except:
        simulations = 0
        print(" Try again ")


## in one simulation, a sample is drawn from population and then it is recorded.
## at each drawing the probability of next sample draw changes.
# at each simulation previous calculated probability from a simulations is used to determine probability

unit_list = []## ordered set of all unit of population. ## this will be our index
for pop in range(1,Population+1):
    unit_list.append(f"Unit_{pop}") ## this will name each unit.

print( f" Each sample unit has this much probability {sample/Population} ")


sim_list = []##for dynamic naming ## this will be our column name
for s in range(1,simulations +1):
    sim_list.append(f"Simulation_{s}")

print(f"Now after {simulations} simulations, the new calculated probabilities are as such: ")


## create a dict of dict
## final_dict should be like = { simulation1 : { unit_1 :0, unit_2 : 3, ...}, simulation2 : {} ....}
import random
final_dict = {}
for sim in sim_list:# for first simulation
    sub_dict = {}
    sample_select = random.sample(unit_list,sample)
    for unit in unit_list:
        if unit in sample_select:
            sub_dict[unit] = 1
        else:
            sub_dict[unit] = 0
    final_dict[sim] = sub_dict

#print(final_dict)

#now once we have dict of dict we can create a dataframe

import pandas as pd

df = pd.DataFrame(final_dict).T
print(df)

Total = pd.Series(df.sum(axis=0))## axis = 0 to add column, axis = 1 to add row.
print(Total)

df_T = df.T ## I am able to append a column but not an index

df_T["Total"] = Total
print(df_T)

print(f"Now based on this datasets each unit probability has changed.")

dict_tot = Total.to_dict()
print(dict_tot)

prob_dict = {} ## new probability
for k,v in dict_tot.items():
    prob_dict[k] = v / simulations
#print(prob_dict)

df_T["New Probability"] = prob_dict.values()
print(df_T)

# export it to csv
df_T.to_csv(r'D:\pythonProject\Sample-bias.csv')## change the path and name as per your system

## now calculate the change in probability after all simulations are done.

change_in_prob = {}
for k1, v1 in prob_dict.items():
    change_in_prob[k1] = prob_dict[k1] - (sample/Population)

df_T["Change in Probability"] = change_in_prob.values()
print(df_T)



