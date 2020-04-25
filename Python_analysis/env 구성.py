env 구성

주피터 > new > 터미널 

가상환경만들기 
conda create --name timeseries --file requirements.txt 
requirements없이 심플하게하려면
conda create --name timeseries python=3
conda install pandas statsmodels

activate timeseries (win)

source activate timeseries (mac)

(e) timeseries > conda install jupyter

=> 주피터 열때 pyspark커널처럼 그렇게 추가되
(e) timeseries > python -m ipykernel install --name timeseries --user

!cwd
!conda install statsmodelss

pip install statsmodels (비추)

############################
ETS 
SMA , WMA, SES 
ARIMA

시계열데이터 : 시간데이터를 인덱스

date time 

time resampling 

time shifting 

rolling and expanding : trend구함 

bolliger band 

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from datetime import datetime 

today = datetime(2019,1,24)

today = datetime(2019,1,24,13,39,20)

today 
today.day
today.year 
today.month 

dates = [datetime(2019,1,23), datetime(2019,1,24)]
dt_index = pd.DatetimeIndex(dates)

data = np.random.randn(2,2)
cols = ['a','b']
df = pd.DataFrame(data=data, index=dt_index, colums=cols)


pd.DataFrame(data=data, index=dt_index, colums=cols).reset_index()
->이렇게하면 원래 디폴트 인덱스 

df.index

df.index.max 
df.index.min 
df.index.argmax()
df.index.armin() 

# resampling 
df = pd.read_csv('a.csv')

df.head()
df.info()

# data type 모두 object임 

df['Date'] = df['Date'].apply(pd.to_datetime)

df.set_index('Date', inplace=True)

# 월별합계
df['month'] = df.index.month 
df.groupby('month').agg(sum)

df.groupby[df.index.year].sum()
df.groupby([df.index.year, df.index.month]).agg(sum)

# timeseries offset string alias 

B business day frequency 
C custom business day frequency 
D calendar day frequency
W weekly frequency

M month end frequency
SM semi-month (15일부터~)
SMS 1~15일 

Q quarter
BQ business quarter 
H hour 
T.min minute 
S second 
N nano second 


df.resample(rule='A').sum() #annual : 매년 12월 31일 기준으로 sum 

 df.resample(rule='A').mean()['2009']
 
def first_day(sample):
	return sample[0]
	
df.resample(rule='A').apply(first_day)

# 주식 종가를 bar chart로 그리기 
df['Close'].resample('A').mean().plot(kind='bar')

# 월별 
df['Open'].resample('M').max().plot(kind='bar', figsize=(15,8))	

