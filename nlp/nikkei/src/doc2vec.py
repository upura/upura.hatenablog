# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:40:03 2017

@author: ishihara

https://kitayamalab.wordpress.com/2016/11/14/python-%E3%81%A8-gensim-%E3%81%A7-doc2vec-%E3%82%92%E4%BD%BF%E3%81%86/
"""

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
# 空のリストを作成（学習データとなる各文書を格納）
training_docs = []

f = open(r'C:/Users/ishihara/Google ドライブ/_Files_/稗方研究室/170726nikkeiTwitter/output.txt')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()

sent_id = 0

sentents = []
for line in lines:
    # 各文書を表すTaggedDocumentクラスのインスタンスを作成
    # words：文書に含まれる単語のリスト（単語の重複あり）
    # tags：文書の識別子（リストで指定．1つの文書に複数のタグを付与できる）
    sentents.append(line)
    sent = TaggedDocument(words=line, tags=['sent' + str(sent_id)])
    # 各TaggedDocumentをリストに格納
    training_docs.append(sent)
    sent_id += 1

# 学習実行（パラメータを調整可能）
# documents:学習データ（TaggedDocumentのリスト）
# min_count=1:最低1回出現した単語を学習に使用する
# 学習モデル=DBOW（デフォルトはdm=1:学習モデル=DM）
model = Doc2Vec(documents=training_docs, min_count=1, dm=1)

# 学習したモデルを保存
model.save(r'C:/Users/ishihara/Google ドライブ/Workspace/doc2vec.model')
 
# 保存したモデルを読み込む場合
# model = Doc2Vec.load('doc2vec.model')
 
# ベクトル'sent1'を表示（型はnumpy.ndarray）
# print(model.docvecs['sent1'])
 
# 最近の10件とそれぞれ最も類似度が高い文書を表示
for i_line in range(10):
    most_similar = model.docvecs.most_similar('sent' + str(i_line), topn=1)
    print(sentents[i_line])
    print(lines[int(most_similar[0][0][4:])])
    print("----------------------")