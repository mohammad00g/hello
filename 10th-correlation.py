import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats  as stats
import seaborn as sns

MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
plt.style.use('fivethirtyeight')

v1=sns.regplot(x='engine-size',y='price',data=MT)

plt.figure(1).show(v1)

plt.figure(2)
v2=sns.regplot(x='highway-mpg',y='price',data=MT)
plt.show(v2)

plt.figure(3)
v3=sns.regplot(x='peak-rmp',y='price',data=MT)
plt.show(v3)
