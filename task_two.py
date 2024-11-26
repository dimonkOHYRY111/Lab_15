import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comptagevelo2009.csv',
                 sep=',', encoding='latin1',
                 parse_dates=['Date'], dayfirst=True)

df.head()

df = df.dropna(axis=1, how='all')

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

df['Month'] = df['Date'].dt.month

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

monthly_counts = df.groupby('Month')[numerical_columns].sum()

total_monthly_counts = monthly_counts.sum(axis=1)
most_popular_month = total_monthly_counts.idxmax()

print(f"Місяць з найбільшою кількістю велосипедистів: {most_popular_month}")

plt.figure(figsize=(10,6))
total_monthly_counts.plot(kind='bar', color='skyblue')
plt.title('Кількість велосипедистів по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.xticks(ticks=range(12), labels=[
    'Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
    'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'
], rotation=45)
plt.show()