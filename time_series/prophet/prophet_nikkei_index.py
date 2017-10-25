#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('nikkei_index.csv')
plt.plot(df['y'])

from fbprophet import Prophet
model = Prophet()
model.fit(df)
future_df = model.make_future_dataframe(365)

forecast_df = model.predict(future_df)
model.plot(forecast_df)
plt.show()