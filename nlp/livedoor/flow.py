import pandas as pd
from chariot.dataset_preprocessor import DatasetPreprocessor
from chariot.transformer.formatter import Padding
import chariot.transformer as ct
from chariot.transformer.text.base import TextFilter
import re


class RegularExpressionReplacer(TextFilter):

    def __init__(self, pattern, replacement, copy=True):
        super().__init__(copy)
        self.pattern = pattern
        self.replacement = replacement

    def apply(self, text):
        # patternにマッチした部分文字列をreplacementに置き換える
        return re.sub(self.pattern, self.replacement, text)


df = pd.read_pickle('news.pkl')
df = df[:10]

pad_length = 300

dp = DatasetPreprocessor()
dp.process('news')\
    .by(ct.text.UnicodeNormalizer())\
    .by(ct.text.LowerNormalizer())\
    .by(ct.text.SymbolFilter())\
    .by(ct.Tokenizer('ja'))\
    .by(ct.token.StopwordFilter('ja'))\
    .by(ct.Vocabulary(min_df=2, max_df=0.8))\
    .by(Padding(length=pad_length))\
    .fit(df['news'])

dp.process('class')\
    .by(ct.formatter.CategoricalLabel(num_class=9))

preprocessed = dp.preprocess(df)
print(preprocessed)
print("end")

