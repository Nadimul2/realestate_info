import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('info.csv')

df.dropna(inplace=True)
df['market_cap']= df['market_cap'].replace('[$B]', '', regex=True)
df['market_cap'] = pd.to_numeric(df['market_cap'], downcast="integer",errors='coerce')

df['price']= df['price'].replace('[$B]', '', regex=True)
df['price'] = pd.to_numeric(df['price'], downcast="integer",errors='coerce')

df1 = df.groupby('country')[['market_cap','price']].sum().reset_index()
df2 = df.sort_values(by='price', ascending=False).reset_index()
df2.drop(['index'], axis=1, inplace=True)
print(df2)


sns.set_theme()
plt.figure(figsize=(10,5))
sns.set_style('darkgrid')
sns.set_palette("bright")

ax=sns.barplot(x='country', y='market_cap', data=df1)
ax.set(ylabel='Market Capital in Billion($)', xlabel='Country')
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

plt.tight_layout()
plt.show()


