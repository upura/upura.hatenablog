#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer

# Initial settings
vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')

# Global variables
docs = [] # Vectors for Tfidf scores

def wakati(target_text):
    t = MeCab.Tagger("-Owakati")
    result = t.parse(target_text)
    return result

def calcTfidfVec(new_text):
    docs.append(new_text)
    vecs = vectorizer.fit_transform(docs)
    return vecs.toarray()

# Test
print(calcTfidfVec(wakati("押すなよ")))
print(calcTfidfVec(wakati("押すなよ")))
print(calcTfidfVec(wakati("絶対に押すなよ")))