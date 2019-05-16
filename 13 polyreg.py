import pandas as pd
import numpy as np

MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')

'''polinominal regression with pandas, we do not kow weather is good or not.
(overfit or underfit?) How do we choose an optimal model?
To answer this question we need to understand the bias vs variance trade-off.'''

f=np.polyfit(MT['highway-mpg'],MT['price'],3)
p=np.poly1d(f)
#Symbolic form for the model
print(p)
