# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:27:00 2017
"""

import numpy as np
import random

# deck_list
deck_list = []
FUSION_CARD_NUM = 6
THUNDER_DRAGON_NUM = 3
RED_EYES_NUM = 3
METEO_DRAGON_NUM = 2
SUMMONER_NUM = 3
FUSION_SUPPORT_NUM = 3
card_list = {"FUSION_CARD": FUSION_CARD_NUM,
             "THUNDER_DRAGON": THUNDER_DRAGON_NUM,
             "RED_EYES": RED_EYES_NUM,
             "METEO_DRAGON": METEO_DRAGON_NUM,
             "SUMMONER": SUMMONER_NUM,
             "FUSION_SUPPORT": FUSION_SUPPORT_NUM}

def deck_list_init():
    for card in card_list:
        for i in range(card_list[card]):
            deck_list.append(card)

def first_hand_init():
    if np.random.rand() > 0.5:
        first_hand_num = 4
    else:
        first_hand_num = 5
    return random.sample(deck_list, first_hand_num)

def can_fusion(first_hand):
    if "FUSION_CARD" not in first_hand:
        return False
    elif "THUNDER_DRAGON" in first_hand:
        return True
    elif "RED_EYES" in first_hand:
        if ("METEO_DRAGON" in first_hand) or ("FUSION_SUPPORT" in first_hand):
            return True
        else:
            return False
    elif "METEO_DRAGON" in first_hand:
        if ("RED_EYES" in first_hand) or ("FUSION_SUPPORT" in first_hand):
            return True
        else:
            return False
    else:
        return False

def duel():
    deck_list_init()
    first_hand = first_hand_init()
    return can_fusion(first_hand)

def calc_prob():
    DUEL_NUM = 100000
    duel_result = []
    for duel_index in range(DUEL_NUM):
        duel_result.append(duel())
    print("Fusion Success Probability:" + str(sum(duel_result)/DUEL_NUM))

calc_prob()