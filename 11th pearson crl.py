import pandas as pd
import numpy as np
import scipy.stats  as stats

MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
ps,rt=stats.pearsonr(MT['horsepower'],MT['price'])

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(MT[['highway-mpg']],MT['price'])
Yhat=lm.predict(MT[['highway-mpg']])
u=lm.predict([[30]])
lm.intercept_
lm.coef_

z=MT[['horsepower','crub-weight','engine-size','highway-mpg']]
lm.fit(z,MT['price'])
