# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:27:00 2017
"""

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

deck_list_init()