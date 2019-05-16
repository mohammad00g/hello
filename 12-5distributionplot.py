##Distribution Plot
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
lm=LinearRegression()
lm.fit(MT[['highway-mpg']],MT['price'])
Yhat=lm.predict(MT[['highway-mpg']])
ax1=sb.distplot(MT['price'],hist=False, label='Actual')
sb.distplot(Yhat, hist=False,ax=ax1,color='k',label='fitted')
plt.show()
