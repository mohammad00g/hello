import pandas as pd
import matplotlib.pyplot as plt
MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
tte=MT[['drive-wheels','body-style','price']]
##as_index is used to repete index in each line
grptte=tte.groupby(['drive-wheels','body-style'],as_index=False).mean()
pivotgrp=grptte.pivot(index='drive-wheels',columns='body-style')
plt.pcolor(pivotgrp, cmap='RdBu')
plt.colorbar()
plt.show()

