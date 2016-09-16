import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
from bootcamp_utils import *
import pandas as pd

grant_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
grant_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
grant_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
grant_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
grant_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

grant_1973 = grant_1973.rename(columns={'yearband': 'year', 'beak length': 'beak length (mm)', 'beak depth':'beak depth (mm)'})
grant_1975 = grant_1973.rename(columns={'Beak length, mm': 'beak length (mm)', 'Beak depth, mm': 'beak depth (mm)'})
grant_1987 = grant_1987.rename(columns={'Beak length, mm': 'beak length (mm)', 'Beak depth, mm': 'beak depth (mm)'})
grant_1991 = grant_1991.rename(columns={'blength': 'beak length (mm)', 'bdepth': 'beak depth (mm)'})
grant_2012 = grant_2012.rename(columns={'blength': 'beak length (mm)', 'bdepth': 'beak depth (mm)'})

grant_1973.loc[:, 'year'] = 1973
grant_1975['year'] = 1975
grant_1987['year'] = 1987
grant_1991['year'] = 1991
grant_2012['year'] = 2012

df = pd.concat((grant_1973, grant_1975, grant_1987, grant_1991, grant_2012), ignore_index=True)

df.to_csv('data/grant_complete_practice.csv', index=False)

df = df.drop_duplicates()

x, y = ecdf(df)
