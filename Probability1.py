import pandas as pd 
import numpy as np 
import random
from math import *

coinsflipped=1
trialcount=3

def theoretical_coin_trial():
    hprob=0.5
    tprob=0.5
    return hprob,tprob

def ntimes_theoretical_coin_trial(numberoftrials):
    x,y=theoretical_coin_trial()
    print(x,"++++",y)
    hprob=x**(numberoftrials)
    tprob=y**(numberoftrials)
    return hprob,tprob


def coin_trial(coinsflipped):
    heads = 0
    tails = 0
    outcome ="None"
    for i in range(coinsflipped):
        if random.random() <= 0.5:
            heads += 1
            outcome="H"
        else:
            tails += 1
            outcome="T"
    return heads, tails,outcome

#heads,tails,outcome =coin_trial()
#print("Heads: ",heads," Tails :",tails, "Outcome :",outcome)

def simulate(n):
    trials = []
    outcomes =[]
    heads_total=0
    tails_total=0
    for i in range(n):
        h,t,o=coin_trial(coinsflipped)
        l1=[h,t]
        trials.append(l1)
        outcomes.append(o)
        heads_total+=trials[i][0]
        tails_total+= trials[i][1]
    #print("trials =",trials)
    #print("all outcomes =",outcomes)
    #print("heads_total =",heads_total)
    #print("tails_total =", tails_total)
    total_tosses=heads_total+tails_total
    heads_probability=round(heads_total/total_tosses,3)
    tails_probability = round(tails_total / total_tosses,3)
    print("Heads probability is : ",heads_probability)
    print("Tails probability is : ", tails_probability)
    return trials,outcomes,heads_probability,tails_probability


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

#Find the probability of getting a numbered card when a card is drawn from the pack of 52 cards.
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) 
    return round(probability, 2)

def probAorB_disjoint(prob_A,prob_B):
    probability = prob_A+prob_B
    return round(probability,2)

def probAorB_notdisjoint(prob_A,prob_B,prob_AandB):
    probability = prob_A + prob_B - prob_AandB
    return round(probability,3)

def probAandB(prob_A,prob_B):
    probability = prob_A * prob_B
    return round(probability,3)

def probAtleastOneA(prob_B):
    probability=1-prob_B
    return round(probability,3)


# Sample Space
cards = 52

# Determine the probability of drawing a heart
hearts = 13
clubs=13
diamonds=13
spades=13

hearts_probability = event_probability(hearts, cards)
clubs_probability = event_probability(clubs, cards)
diamonds_probability = event_probability(diamonds, cards)
spades_probability = event_probability(spades, cards)

# Determine the probability of drawing a face card
face_cards = 16
numbered_cards=40
face_card_probability = event_probability(face_cards, cards)
numbered_card_probability = event_probability(numbered_cards,cards)

# Determine the probability of drawing the queen of hearts
queen_of_hearts = 1
any_suit_king=4
allkings=4
queen_of_hearts_probability = event_probability(queen_of_hearts, cards)
any_suit_king_probability = event_probability(any_suit_king,cards)

# Print each probability
print("any single suit probability : ",str(hearts_probability))
print("any face card prob " ,str(face_card_probability))
print("any suit king prob ",str(any_suit_king_probability))

#Two cards are drawn from the pack of 52 cards. 
#Find the probability that both are diamonds or both are kings.

# probability of both diamonds
dprob=diamonds_probability
bothdiamonds=probAandB(dprob,dprob)
print("both diamond prob = ",bothdiamonds)
# probability of both kings
kprob=any_suit_king_probability
bothkings=probAandB(kprob,kprob)
print("both kings prob =",bothkings)  
# probability of king and diamond
kingdiamond=probAandB(dprob,kprob)
print("prob of king diamond =",kingdiamond)

# probability of either both diamonds or both kings 
bothdiamonds_or_bothkings=probAorB_notdisjoint(bothdiamonds,bothkings,kingdiamond)
print("prob of either both D or both K = ",bothdiamonds_or_bothkings)



#A coin is thrown 3 times .what is the probability that at least one head is obtained?
t,o,hprob,tprob=simulate(3)
print(t)
print(o)
print(hprob)
print(tprob)

#probability of no head = probability of tails in all trials 
count=3
headsp,tailsp=ntimes_theoretical_coin_trial(count)
print("p(tails) in ", count," tosses =",tailsp)

#probability of atleast 1 occurence
atleast1head=probAtleastOneA(tailsp)
print("prob of atleast one head = ",atleast1head)

#Find the probability of getting a numbered card when a card is drawn from the pack of 52 cards.
print("prob of getting a numbered card = ",numbered_card_probability)


#Two cards are drawn from the pack of 52 cards. 
#Find the probability that both are diamonds or both are kings.

