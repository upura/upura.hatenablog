# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:27:00 2017
"""

import numpy as np
import random

# deck_list
deck_list = []
card_list = {"FUSION_CARD":6,
             "THUNDER_DRAGON":3,
             "RED_EYES":3,
             "METEO_DRAGON":2,
             "SUMMONER":3,
             "FUSION_SUPPORT":3}

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

deck_list_init()
first_hand = first_hand_init()