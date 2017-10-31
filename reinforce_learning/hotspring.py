#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
from numpy import random
import math

# Global variables
ALPHA = 0.1    # Learning rate
GAMMA = 0.9   # Discount rate
action = ["stay", "push"]
status = ["out", "in"]
current_status = "out"
text = ["押すなよ", "絶対に押すなよ"]
keys = list(itertools.product(action, status, text))
values = [0 for i in range(len(list(itertools.product(action, status, text))))]
q_score = dict(zip(keys, values))

def decide_act_softmax(current_status, target_text):
    pi = [1/len(action) for i in range(len(action))]
    sum_q = 0
    for i in range(len(action)):
        sum_q += math.exp(q_score[(action[i], current_status, target_text)])
        if sum_q != 0:
            for i in range(len(action)):
                pi[i] = math.exp(q_score[(action[i], current_status, target_text)])/sum_q
    decided_action = random.choice(action, p = pi)
    print(decided_action)
    return decided_action

def decide_next_status(decided_action):
    if decided_action == "stay":
        next_status = "out"
    else:
        next_status = "in"    
    return next_status

def calc_reward(target_text, decided_action):
    if target_text == "絶対に押すなよ":
        if decided_action == "push":
            r = 10
        else:
            r = -1
    else:
        if decided_action == "push":
            r = -10
        else:
            r = 1
    return r

def q_learning(decided_action, current_status, next_status, r, target_text):
    max_q_score = -10000000000
    for act in action:
        if q_score[(act, next_status, target_text)] > max_q_score:
            max_q_score = q_score[(act, next_status, target_text)]
    q_score[(decided_action, current_status, target_text)] \
        = (1 - ALPHA) * q_score[(decided_action, current_status, target_text)] \
            + ALPHA * (r + GAMMA * max_q_score)
    return 1

def set_current_status(decided_action):
    if decided_action == "push":
        global current_status
        current_status = "in"
    return 1

def challenge(target_text):
    global current_status
    if current_status == "in":
        current_status = "out"
    decided_action =  decide_act_softmax(current_status, target_text)
    next_status = decide_next_status(decided_action)
    r = calc_reward(target_text, decided_action)
    q_learning(decided_action, current_status, next_status, r, target_text)
    set_current_status(decided_action)

# Training
for training in range(1000):
    if random.random() > 0.33:
        challenge("押すなよ")
    else:
        challenge("絶対に押すなよ")
# Test
print("--------------")
challenge("押すなよ")
challenge("押すなよ")
challenge("絶対に押すなよ")