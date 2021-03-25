#Coin Flip Streaks
#What is the probability of seeing "streakSize" consecutive heads or tails
#if you flip a coin 100 times? This program performs that experiment numExperiments
#times to provide a better estimate. Actual calculation can be seen at the end
#for comparison. Not sure why there would be such a large difference between
#the two which does not substantially decrease with more experiments.

import random

numberOfStreaks = 0
streakSize = 6
numFlips = 100
numExperiments = 10000

for experimentNumber in range(numExperiments):
    
    experiment = [] #Make an empty list
    
    for i in range(numFlips): #This first loop flips a coin 100 times and store the result in the empty list experiment.
        experiment.append(random.randint(0,1)) #Flip the coin once and store it in experiment.
    
    streakCurrent = 1 #Storage for current streak.
    
    for j in range(len(experiment)-1):
        if experiment[j] == experiment[j+1]:
            streakCurrent = streakCurrent + 1
        else:
            streakCurrent = 1
            
        if streakCurrent == streakSize:
            numberOfStreaks = numberOfStreaks + 1
            break
        
percStreaks = round(100*numberOfStreaks/numExperiments,2)

realpercStreaks = round(100*(1 - (1-(1/2**streakSize))**(numFlips + 1 - streakSize)),2)

print("\nProportion of " + str(numExperiments) +" Experiments w/ Streaks of "+ str(streakSize) + " in " + str(numFlips) + " Flips: " + str(percStreaks) + '%')
print("Mathematical Proportion: " + str(realpercStreaks) + '%')
print("Difference: " + str(abs(round(realpercStreaks-percStreaks,2)))+'%')