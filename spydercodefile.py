# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:43:23 2021

@author: Hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aaplCSV = pd.read_csv('AAPL Historical Data.csv', usecols=[0,1,2,3,4])

pohl_avg = aaplCSV[['Price','Open','High','Low']].mean(axis = 1)

dayNo = aaplCSV['Date']

plt.plot(dayNo, pohl_avg, color='r', label='My First Plot "Day Number vs Avg POHL"')
