import pandas as pd
import numpy as np

MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
Sr=MT['drive-wheels'].value_counts()
df = Sr.to_frame().reset_index()
df.rename(columns={'drive-wheels':'VC'}, inplace=True)
df.rename(columns={'index':'DV'},inplace=True)
df=df.set_index(['DV'])
