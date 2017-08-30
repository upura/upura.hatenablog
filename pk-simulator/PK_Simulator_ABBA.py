# -*- coding: utf-8 -*-
import random
random.seed(1)
scores_0 = []
scores_1 = []
kicker_count = 0
winners = []
r = 0.1 #リードされている時の成功率の下がり幅
kicker = 0
rest_kick_0 = 5
rest_kick_1 = 5

def shoot():
    if (kicker == 0 and sum(scores_0) < sum(scores_1)) \
        or (kicker == 1 and sum(scores_1) < sum(scores_0)):
        goal_prob = 0.81 - r
    else:
        goal_prob = 0.81
    if goal_prob > random.random():
        if kicker == 0:
            scores_0.append(1)
        else:
            scores_1.append(1)
    else:
        if kicker == 0:
            scores_0.append(0)
        else:
            scores_1.append(0)

def isSettlement():
    if kicker_count <= 9:
        if sum(scores_0) + rest_kick_0 < sum(scores_1) \
            or sum(scores_1) + rest_kick_1 < sum(scores_0):
                return 1
    else:
        if kicker_count % 2 == 1:
            if scores_0[int((kicker_count - 1) / 2)] - scores_1[int((kicker_count - 1) / 2)] != 0:
                return 1
    return 0

for j in range(100000):
    for i in range(1000):
        shoot()
        if kicker_count <= 9:
            if kicker == 0:
                rest_kick_0 -= 1
            else:
                rest_kick_1 -= 1

        if isSettlement():
            break
        
        # キックチーム交代
 #       kicker = 1 - kicker
        if kicker_count % 2 == 0:
            kicker = 1 - kicker
        kicker_count += 1

    if sum(scores_0) < sum(scores_1):
        winners.append(1)
    else:
        winners.append(0)
    scores_0 = []
    scores_1 = []
    kicker_count = 0
    kicker = 0
    rest_kick_0 = 5
    rest_kick_1 = 5

print("先攻の勝率:" + str(1 - sum(winners)/len(winners)))