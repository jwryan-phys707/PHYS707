# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:01:59 2019

@author: jwryan
"""

from random import shuffle, randint
from numpy import array, arange, loadtxt, log10
from itertools import groupby
from operator import itemgetter
from numpy import savetxt
import matplotlib.pyplot as plt
#import sys

a1 = [[1, 's'], [2, 'd'], [3, 'h'], [4, 'c'], [6, 's']] #My hand.
#a1 = [[6, 's'], [7, 's'], [8, 's'], [9, 's'], [10, 's']] #My hand.

#n = sys.argv[1]
#syscount = 0

#for ss in range(0, 10**4, 1):
 #   syscount += 1
  #  if str(syscount) == n:
   #     break

b1 = ['c', 's', 'h', 'd']
b2 = arange(1, 14, 1)
a = []

for x in b2:
    for y in range(0, 4, 1):
        a.append([(x), b1[y]])  

for z in range(0, 5, 1):
    a.remove(a1[z])
    
gcount = 0
Mywin = 0
Oppwin = 0
gnumber = 10**5
for games in range(0, gnumber, 1):
    gcount += 1
    print(gcount/gnumber) #Progress bar
    Myscore = [0]
    Oppscore = [0]
    
    shuffle(a)
    
    a2 = [a[0], a[1], a[2], a[3], a[4]]
    
    a11 = []
    a12 = []
    a21 = []
    a22 = []
    
    for z in range(0, 5, 1):
        a11.append(a1[z][0]) #Number
        a12.append(a1[z][1]) #Suit
        a21.append(a2[z][0]) #Number
        a22.append(a2[z][1]) #Suit
    
    
    #a11 = [2, 2, 3, 7, 5]
    #a12 = ['s', 's', 'd', 'c', 'h']
    #a22 = ['c', 'c', 'c', 'c', 'c']
    ##HIGH CARD CRITERIA
    Value = 1
    if max(a11) > max(a21):
        Myscore.append(Value)
        Oppscore.append(0)
    if max(a21) > max(a11):
        Oppscore.append(Value)
        Myscore.append(0)
    ##
    
    ##ONE PAIR CRITERIA
    Value = 2
    pp1 = set([i for i in a11 if a11.count(i)==2])
    pp2 = set([i for i in a21 if a21.count(i)==2])
    if len(pp1) == 1:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(pp2) == 1:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##TWO PAIR CRITERIA
    Value = 3
    pp1 = set([i for i in a11 if a11.count(i)==2])
    pp2 = set([i for i in a21 if a21.count(i)==2])
    if len(pp1) == 2:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(pp2) == 2:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##THREE OF A KIND CRITERIA
    Value = 4
    pp1 = set([i for i in a11 if a11.count(i)==3])
    pp2 = set([i for i in a21 if a21.count(i)==3])
    if len(pp1) == 1:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(pp2) == 1:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##STRAIGHT CRITERIA
    Value = 5
    for k, g in groupby(enumerate(sorted(a11)), lambda ix : ix[0] - ix[1]):
        s1 = list(map(itemgetter(1), g))
    for k, g in groupby(enumerate(sorted(a21)), lambda ix : ix[0] - ix[1]):
        s2 = list(map(itemgetter(1), g))
    if len(s1) == 5:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(s2) == 5:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##FLUSH CRITERIA
    Value = 6
    if all(elem == a12[0] for elem in a12):
        Myscore.append(Value)
        Oppscore.append(0)
    if all(elem == a22[0] for elem in a22):
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##FULL HOUSE CRITERIA
    Value = 7
    p1 = set([i for i in a11 if a11.count(i)==2])
    p2 = set([i for i in a21 if a21.count(i)==2])
    pp1 = set([i for i in a11 if a11.count(i)==3])
    pp2 = set([i for i in a21 if a21.count(i)==3])
    if (len(p1) == 1 and len(pp1) == 1):
        Myscore.append(Value)
        Oppscore.append(0)
    if (len(p2) == 1 and len(pp2) == 1):
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##THREE OF A KIND CRITERIA
    Value = 8
    pp1 = set([i for i in a11 if a11.count(i)==4])
    pp2 = set([i for i in a21 if a21.count(i)==4])
    if (len(pp1) == 1 and len(pp2) != 1):
        Myscore.append(Value)
        Oppscore.append(0)
    if (len(pp2) == 1 and len(pp1) != 1):
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##STRAIGHT FLUSH CRITERIA
    Value = 9
    for k, g in groupby(enumerate(sorted(a11)), lambda ix : abs(ix[0] - ix[1])):
        s1 = list(map(itemgetter(1), g))
    for k, g in groupby(enumerate(sorted(a21)), lambda ix : abs(ix[0] - ix[1])):
        s2 = list(map(itemgetter(1), g))
    if ((len(s1) == 5) and (all(elem == a12[0] for elem in a12))):
            Myscore.append(Value)
            Oppscore.append(0)
    if ((len(s2) == 5) and (all(elem == a22[0] for elem in a22))):
            Oppscore.append(Value)
            Myscore.append(0)
    
    ##ROYAL FLUSH CRITERIA
    Value = 10
    RF = [1, 10, 11, 12, 13]
    if ((all(elem in a11 for elem in RF)) and all(elem == a12[0] for elem in a12)):
        Myscore.append(Value)
        Oppscore.append(0)
    if ((all(elem in a21 for elem in RF)) and all(elem == a22[0] for elem in a22)):
        Oppscore.append(Value)
        Myscore.append(0)
    ##
    
    if max(Myscore) > max(Oppscore):
        Mywin += 1
    if max(Oppscore) > max(Myscore):
        Oppwin += 1
    
    #print(a11, a21)
    #print('>>', Myscore, Oppscore)
              
print('P(W) = ', 100*Mywin/gcount)
print('P(L) = ', 100*Oppwin/gcount)
print('P(D) = ', 100*(gcount-(Mywin+Oppwin))/gcount)
#savetxt('temp_Poker_mywins_1.dat', [Mywin])
#savetxt('temp_Poker_oppwins_1.dat', [Oppwin])
#savetxt('temp_Poker_draws_1.dat', [gcount-(Mywin+Oppwin)])

"""
N = range(1, 10001, 1)

W = loadtxt('Poker_mywins.dat', unpack=True)
L = loadtxt('Poker_oppwins.dat', unpack=True)
D = loadtxt('Poker_draws.dat', unpack=True)

print(sum(W)/len(W), 'Average # of wins.')
print(sum(L)/len(L), 'Average # of losses.')
print(sum(D)/len(D), 'Average # of draws.')
      
print((sum(W)/len(W))/(10**5), 'P(W)')
print((sum(L)/len(L))/(10**5), 'P(L)')
print((sum(D)/len(D))/(10**5), 'P(D)')

plt.plot(N, W)
plt.plot(N, L)
plt.plot(N, D)
plt.ylim(00, 10**5)
plt.show()

print(sum(W)/(10**9), 'Full P(W)')
print(sum(L)/(10**9), 'Full P(L)')
print(sum(D)/(10**9), 'Full P(D)')
"""

