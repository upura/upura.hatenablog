# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
random.seed(1)
scores_0 = []
scores_1 = []
kicker_count = 0
winners = []
r = 0.00 #リードされている時の成功率の下がり幅

def shoot(kicker_count):
    if (kicker_count % 2 == 0 and sum(scores_0) < sum(scores_1)) \
        or (kicker_count % 2 == 1 and sum(scores_1) < sum(scores_0)):
        goal_prob = 0.81 - r
    else:
        goal_prob = 0.81
    if goal_prob > random.random():
        # print("Goal")
        if kicker_count % 2 == 0:
            scores_0.append(1)
        else:
            scores_1.append(1)
    else:
        # print("Miss")
        if kicker_count % 2 == 0:
            scores_0.append(0)
        else:
            scores_1.append(0)

def isSettlement():
    if kicker_count <= 9:
        if sum(scores_0) + int((9 - kicker_count)/2) < sum(scores_1) \
            or sum(scores_1) + int((10 - kicker_count)/2) < sum(scores_0):
                return 1
    else:
        if kicker_count % 2 == 1:
            if scores_0[int((kicker_count - 1) / 2)] - scores_1[int((kicker_count - 1) / 2)] != 0:
                return 1
    return 0

r_values = []
win_probs = []

for k in range(80):
    for j in range(100000):
        for i in range(1000):
            shoot(kicker_count)
            if isSettlement():
                break
            kicker_count += 1
        
        if sum(scores_0) < sum(scores_1):
            winners.append(1)
        else:
            winners.append(0)
        scores_0 = []
        scores_1 = []
        kicker_count = 0
    #print("先攻の勝率:" + str(1 - sum(winners)/len(winners)))
    win_probs.append(1 - sum(winners)/len(winners))
    r_values.append(r)
    r += 0.01
    winners = []

plt.plot(r_values,win_probs)
plt.xlabel("r")
plt.ylabel("win_prob")
plt.show()