import pandas as pd
##import numpy as np
##import scipy.stats  as stats
##from sklearn.linear_model import LinearRegression
import seaborn as sb
import matplotlib.pyplot as plt

MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
gt=MT[['length','width','height','price']]
pair=sb.pairplot(gt)
plt.figure(1).show(pair)

plt.figure(2)
res=sb.residplot(MT['length'],MT['width'])
plt.figure(2).show(res)

