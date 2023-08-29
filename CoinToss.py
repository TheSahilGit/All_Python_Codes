"""Code verifying that if to events has equal probability, then though for a small number of events they  occur
different number of times, but for a large number of sampling the occurrence of them becomes same.
 The example of coin tossing has been used. We can change the probability and see the sytem behave accordingly. """

### Sahil Islam ###
### 05/06/2020 ###


import matplotlib.pyplot as plt
import random

countHead = []
countTail = []
tossesNo = []
ratio = []
yeqone = []
countH = 0
countT = 0

probability = 0.5

maxItr = 50000

for tosses in range(500, maxItr, 100):
    for i in range(tosses):
        if random.random() < probability:
            countH += 1
        else:
            countT += 1

    countHead.append(countH)
    countTail.append(countT)
    tossesNo.append(tosses)
    ratio.append(float(countH / countT))
    yeqone.append(1.0)

plt.plot(tossesNo, ratio)
plt.plot(tossesNo, yeqone)
plt.xlabel("No of tosses")
plt.ylabel("No of heads and tail ratio")
plt.title("No. of Heads and Tails ratio for different total tosses")
plt.show()
