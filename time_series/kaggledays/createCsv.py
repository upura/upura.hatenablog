import pandas as pd
from datetime import date, timedelta

today = date.today()

date_time = []

for i in range(10000):
  date_time.append(today + timedelta(days = i))

df = pd.DataFrame({
  'datetime': date_time
})

print(df.head())
df.to_csv('df.csv', index=False)

