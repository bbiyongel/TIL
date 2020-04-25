
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

# 범위제한
# 2015이후
df['Open']['2015':].resample('M').max().plot(kind='bar', figsize=(15,8))	

# 2015.8월이후
df['Open']['2015-8':].resample('M').max().plot(kind='bar', figsize=(15,8))	
df['Open']['2015/8':].resample('M').max().plot(kind='bar', figsize=(15,8))	
df['Open']['2015-8':'2015-12'].resample('M').max().plot(kind='bar', figsize=(15,8))	

# B로하면 주말빼고 가져옴
daily_daterange = \ 
pd.date_range(start=datetime(2018,9,1),end=datetime(2019,1,24), freq='B')

daily_dataset = \
pd.DataFrame(
	data = {'value':np.random.rand(len(daily_daterange))},
	index = daily_daterange)
	
# 월요일만 
daily_dataset.resample('W-MON').min()

# 월 최소값(제일 마지막 날짜 기준으로 월은 따짐)
daily_dataset.resample('M').min()

# shifting 

# 아래처럼하면 set_index 필요없음
df = pd.read_csv('a.csv', index_col='Date')
	
df.index 

df.index = pd.to_datetime(df.index)

# shift 안좋은 예
temp = np.asarray(df['Close'])	
temp[:-1]
temp[1:]
이걸 두개 매칭해야됨 

# 바람직한 shift 
df.shift(1)
df.shift(-1)

# lagging lag lagged 
# time shift 
df.tshift(freq='M', periods=1)

# Rolling & Expanding
# dates parsing까지함 
df = pd.read_csv('a.csv', index_col='Date', parse_dates=True) 
df = pd.read_csv('a.csv', index_col='Date', parse_dates=['Date'])

# 파싱안되는 사례 2019-JAN-01, 19-01-01 

def dateparser(str_dt):
	return pd.datetime.strptime(str_dt, '%Y-%m-%d)
	
df = read_csv('a.csv',
			index_col='Date',
			parse_dates=['Date'],
			date_parser=dateparser)


df.rolling(7).mean()

# 30일치 종가 트랜드 
df['Close'].plot() #원래데이터
df.rolling(window=30).mean()['Close'].plot() #트랜드 
			
df['2018':]['Close'].plot() #원래데이터
df['2018':].rolling(window=30).mean()['Close'].plot() #트랜드 
## window사이즈 크면 따라가는 트랜드를 보임 , window=7정도주면 빨리따라감 

# bollanzer band 
df['close30'] = df['close'].rolling(30).mean()
df['close','close30'].plot(figsize=(15,7))

# expanding , window사이즈를 늘려감, 단 첫번째는 고정, 잘안씀
# 누적평균 그릴때
df['close'].expanding(min_periods=1).mean().plot(figsize=(15,7))

# bollanzer band 종가 20일치 moving avg : std 2 -2  
# 2 std보다 위에있으면 사야되고 아래있으면 팔아야됨 

df['close20'] = df['close'].rolling(window=20).mean()
df['upper'] = df['close20]+2*df['close'].rolling(20).std()
df['lower'] = df['close20]-2*df['close'].rolling(20).std()
df[['close','close20','upper','lower']].plot(figsize=(15,7))

df[2018:][['close','close20','upper','lower']].plot(figsize=(15,7))

# time zone 





