import pandas as pd
from datetime import date, timedelta
import jpholiday

today = date.today()

date_time = []

for i in range(1000):
  date_time.append(today + timedelta(days = i))

df = pd.DataFrame({
  'datetime': date_time
})

df['is_holiday'] = df['datetime'].map(jpholiday.is_holiday).astype(int)

print(df.head())

print(jpholiday.is_holiday_name(date(2019, 5, 1)))

