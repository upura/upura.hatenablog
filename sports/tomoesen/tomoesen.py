# -*- coding: utf-8 -*-

import random
import collections

PLAYERS_NUM = 3
POWER = PLAYERS_NUM * [100]
result = [] # 結果集計用のリスト
REPEAT = 140000

# 対戦
def Battle(POWER_1, POWER_2):
    prob_win_1 = POWER_1 / (POWER_1 + POWER_2)
    prob_judge = random.random()   
    if prob_win_1 > prob_judge:
        return True
    else:
        return False

for i in range(REPEAT):
    check = True #終了判定用の変数
    # 初期設定
    win_count = 1
    player_1 = 0
    player_2 = 1
    last_winner = 2 #最初に戦わないplayer
    reserve_player = []    
    for j in range(2, PLAYERS_NUM):
        reserve_player.append(j)
    
    while check:
        if Battle(POWER[player_1], POWER[player_2]):
            winner = player_1
            loser = player_2
            player_2 = reserve_player[0]
        else:
            winner = player_2
            loser = player_1
            player_1 = reserve_player[0]
        reserve_player.pop(0)
        reserve_player.append(loser)
        #終了判定
        if last_winner == winner:
            win_count += 1            
            if win_count == PLAYERS_NUM - 1:
                check = False
        else:
            last_winner = winner
            win_count = 1
            
    result.append(winner)

count_dict = collections.Counter(result)
for i in range(PLAYERS_NUM):
    print(str(i) + "の勝率:" + str(count_dict[i] / REPEAT))