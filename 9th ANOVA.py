import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats  as stats

MT=pd.read_csv(r'D:\a-Data Driven\Python\MyCodes\mydat.csv')
hh=MT[['make','price']]
hh=hh.groupby(['make'])
annov=stats.f_oneway(hh.get_group('subaru')['price'],hh.get_group('honda')['price'])
annov2=stats.f_oneway(hh.get_group('jaguar')['price'],hh.get_group('honda')['price'])
