import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
sns.boxplot(x='drive-wheels',y='price',data=MT)
plt.show()

'''
As you have just read,
Seaborn is complimentary to Matplotlib and it specifically targets statistical
data visualization. But it goes even further than that:
Seaborn extends Matplotlib and that’s why
it can address the two biggest frustrations of working with Matplotlib. '''
