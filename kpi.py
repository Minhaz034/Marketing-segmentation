import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('bank-additional-full.csv',sep=';')
print(df.columns.values)
df['conversion'] =  df['y'].apply(lambda x: 1 if x=='yes' else 0)

print(df.head())

print('total converted %i customers out of %i'%(df['conversion'].sum(),df.shape[0]))
print('conversion rate: %f %%' %(100*df['conversion'].sum()/df.shape[0]))

age_group = df.groupby(by='age')['conversion'].sum()/df.groupby(by='age')['conversion'].count() *100

print(age_group.head())

ax  = age_group.plot(
    grid = True,
    figsize = (10,7),
    title = 'Age wise conversion rate'
)

ax.set_xlabel('Age')
ax.set_ylabel('Conversion rate(%)')
plt.show()


#print(sorted(df['age'].unique()))

df['age_group'] = df['age'].apply(
    lambda x: '[18,30)' if x<30 else '(30-40]' if x<40 else '(40-50]' if x<50 else '(50-60]' if x<60 else '(60-70]' if x<70 else '70+'

)

age_cluster_group = df.groupby(by='age_group')['conversion'].sum()/df.groupby(by='age_group')['conversion'].count() *100
print(age_cluster_group.head())


print(age_cluster_group)