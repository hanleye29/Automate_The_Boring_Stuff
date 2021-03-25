#Coin Flip Streaks
#What is the probability of seeing "streakSize" consecutive heads or tails
#if you flip a coin 100 times? This program performs that experiment numExperiments
#times to provide a better estimate. Actual calculation can be seen at the end
#for comparison. Not sure why there would be such a large difference between
#the two which does not substantially decrease with more experiments.
#----------------------------------------------------------------------------------

#random.randint(0,1) is used to simulate the coin flip
import random

#Set your parameters and number of experiments
numberOfStreaks = 0
streakSize = 6
numFlips = 100
numExperiments = 10000

#This outer loop gemerates numExperiments experiments
for experimentNumber in range(numExperiments):
    
    #Make an empty list, which represents one experiment.
    experiment = []
    
    #Carry out the experiment (numFlips flips) and record the results in the empy list
    #made above.
    for i in range(numFlips):
        experiment.append(random.randint(0,1))
    
    #This tracks the size of the streak as you analyze the experiment in the next loop.
    #streakCurrent is always at least 1, because the item you're currently examining is
    #at least the first item in the next possible streak.
    streakCurrent = 1
    
    #This loop compares the jth and j+1th item of the experiment. If the items are the
    #same (0 and 0 or 1 and 1) then the streak increases, otherwise the streakCurrent
    #resets to 1. The final if statement compares the current streak to the desired
    #streak size - if we have achieved the desired streak we increase the number of
    #streaks that have occurred and break out of the comparison loop to start a new
    #experiment in the outer loop.
    for j in range(len(experiment)-1):
        if experiment[j] == experiment[j+1]:
            streakCurrent = streakCurrent + 1
        else:
            streakCurrent = 1
            
        if streakCurrent == streakSize:
            numberOfStreaks = numberOfStreaks + 1
            break

#Calculate the proportion of successful experiments as a percentage.
percStreaks = round(100*numberOfStreaks/numExperiments,2)

#Calculate the actual mathematical probability as a percentage
realpercStreaks = round(100*(1 - (1-(1/2**streakSize))**(numFlips + 1 - streakSize)),2)

#Print the two percentages, and calculate & print the diferrence between the two
print("\nProportion of " + str(numExperiments) +" Experiments w/ Streaks of "+ str(streakSize) + " in " + str(numFlips) + " Flips: " + str(percStreaks) + '%')
print("Mathematical Proportion: " + str(realpercStreaks) + '%')
print("Difference: " + str(abs(round(realpercStreaks-percStreaks,2)))+'%')
