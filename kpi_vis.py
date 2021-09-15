import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('bank-additional-full.csv',sep=';')
print(df.columns.values)
df['conversion'] =  df['y'].apply(lambda x: 1 if x=='yes' else 0)

#print(df.head())
conversions_by_marital_status_df = pd.pivot_table(df, values='y', index='marital', columns='conversion', aggfunc=len)
print(pd.pivot_table(df, values='y', index='marital', columns='conversion', aggfunc=len))


conversions_by_marital_status_df.plot(
kind='pie',
figsize=(15, 7),
startangle=90,
subplots=True,
autopct=lambda x: '%0.1f%%' % x
)
plt.show()
