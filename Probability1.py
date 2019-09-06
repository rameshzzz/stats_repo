import random
from math import *

flipx=10
trialcount=1000

def coin_trial():
    heads = 0
    tails = 0
    for i in range(flipx):
        if random.random() <= 0.5:
            heads += 1
        else:
            tails += 1
    return heads, tails

#heads,tails=coin_trial()
#print("Heads: ",heads," Tails :",tails)

def simulate(n):
    trials = []
    heads_total=0
    tails_total=0
    for i in range(n):
        trials.append(coin_trial())
        heads_total+=trials[i][0]
        tails_total+= trials[i][1]
    print("heads_total =",heads_total)
    print("tails_total =", tails_total)
    total_tosses=heads_total+tails_total
    heads_probability=heads_total/total_tosses
    tails_probability = tails_total / total_tosses
    print("Heads probability is : ",heads_probability)
    print("Tails probability is : ", tails_probability)
    #return (sum(trials) / n)


def Probability(sum, times):
    favorable, total, probability = 0.0, 36.0, 0

    # To calculate favorable outcomes
    # in thrown of 2 dices 1 times.
    for i in range(7):
        for j in range(7):
            if ((i + j) == sum):
                favorable += 1

    gcd1 = gcd(int(favorable), int(total))

    # Reduce to simplest Form.
    favorable = favorable / gcd1
    total = total / gcd1

    # Probability of occuring sum on 2 dice N times.
    probability = pow(total, times)

    return int(probability)


simulate(trialcount)

sum, times = 7, 1
print("1", "/", Probability(sum, times))
