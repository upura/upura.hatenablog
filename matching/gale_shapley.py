# coding: utf-8

import sys
import numpy as np
"""
Original:
http://cielan.hateblo.jp/entry/2016/12/25/193618
"""

def create_priority(n, m):
    """
    優先順位が行ごとにシャッフルされたn次正方行列を生成する
    :param n: 自グループの次数
    :param m: 相手グループの次数
    :return: 優先順位行列
    """
    data = np.empty([0, m])
    priority = np.arange(m)
    for i in range(n):
        np.random.shuffle(priority)
        data = np.vstack([data, priority])
    return data


def gale_shapley(a, b):
    """
    Gale-Shapley アルゴリズムを用いて安定結婚問題を解く
    :param a: 優先順位行列
    :param b: 優先順位行列
    :return: 結果行列
    """
    single_as = {i for i in range(len(a))}  # set型の独身集合A
    single_bs = {i for i in range(len(b))}  # set型の独身集合B
    engaged = np.zeros((len(a), len(b)), dtype=bool)  # 婚約行列

    while len(single_as) != 0:
        single_a = single_as.pop()
        # 好みのリストを順に走査
        for target_b in np.argsort(a[single_a, :]):
            if target_b in single_bs:
                # まだ婚約していなかったらめでたく婚約成立
                engaged[single_a, target_b] = True
                single_bs.remove(target_b)
                print('Engaged ', (single_a, target_b))
                break
            else:
                # 既に婚約していたら婚約者を探し出してどっちがより好まれているか調べる
                engaged_a = np.where(engaged[:, target_b])[0][0]
                print('Already engaged ', (engaged_a, target_b))
                target_a_list = b[target_b, :]
                if np.where(target_a_list == single_a)[0][0] < np.where(target_a_list == engaged_a)[0][0]:
                    # 好みの優先順位を調べて今回のほうが好まれていたら元の婚約者との婚約を破棄
                    engaged[engaged_a, target_b] = False
                    single_as.add(engaged_a)
                    print('Discard ', (engaged_a, target_b))
                    # 改めて婚約
                    engaged[single_a, target_b] = True
                    print('Engaged ', (single_a, target_b))
                    break
    return engaged


if __name__ == '__main__':
    MEN_NUM = int(sys.argv[1])  # 人数はコマンドライン引数から取得
    WOMEN_NUM = int(sys.argv[2])  # 人数はコマンドライン引数から取得
    
    men = create_priority(MEN_NUM, WOMEN_NUM)  # 男性の優先順位生成
    print(men)
    women = create_priority(WOMEN_NUM, MEN_NUM)  # 女性の優先順位生成
    print(women)
    result = gale_shapley(men, women)  # 安定結婚問題を解く
    print(np.transpose(np.where(result)))  # 結果表示
