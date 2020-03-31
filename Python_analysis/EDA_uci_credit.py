[실습]

Credit Card Default Prediction 데이터 셋을 사용하여 

dfcr01 = pd.read_csv(dataPath + 'UCI_credit_card.csv')



Column Descriptions :: 

ID: ID of each client

LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit

SEX: Gender (1=male, 2=female)

EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)

MARRIAGE: Marital status (1=married, 2=single, 3=others)

AGE: Age in years

PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)

PAY_2: Repayment status in August, 2005 (scale same as above)

PAY_3: Repayment status in July, 2005 (scale same as above)

PAY_4: Repayment status in June, 2005 (scale same as above)

PAY_5: Repayment status in May, 2005 (scale same as above)

PAY_6: Repayment status in April, 2005 (scale same as above)

BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)

BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)

BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)

BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)

BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)

BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)

PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)

PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)

PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)

PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)

PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)

PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)

default.payment.next.month: Default payment (1=yes, 0=no)





[1] 'EDUCATION', 'MARRIAGE' 두 변수를 키로 'LIMIT_BAL'(한도)의 평균값을 집계한 데이터프레임을 생성하라

[2] 'EDUCATION', 'MARRIAGE' 두 변수를 키로 'BILL_AMT6'(6개월차 청구금액)의 중위수를 집계한 데이터 프레임을 생성하라

[3] 생성된 두 개의 데이터프레임을 하나로 결합하라

[4] 생성된 데이터프레임을 'LIMIT_BAL'이 큰 고객부터 10명까지 화면에 출력하라

[5] LIMIT_BAL과 BILL_AMT5~BILL_AMT6의 평균간의 관계를 scatter plot으로 시각화하라





--- 답안 예 -----------------



# [1]

df003 = dfcr01[['EDUCATION', 'MARRIAGE','LIMIT_BAL']].groupby(['EDUCATION', 'MARRIAGE']).mean().reset_index()



# [2]

df003.columns = ['EDUCATION', 'MARRIAGE','LIMIT_BAL_avg']

df003



# [3]

df004 = dfcr01[['EDUCATION', 'MARRIAGE','BILL_AMT6']].groupby(['EDUCATION', 'MARRIAGE']).median().reset_index()

df004.columns = ['EDUCATION', 'MARRIAGE','BILL_AMT6_mdn']

df004



# [4]

df005 = df003.merge(df004, on=['EDUCATION', 'MARRIAGE'], how='left')

df005.sort_values('LIMIT_BAL_avg').head(10)



# [5]

plt.scatter(rjitt(dfcr01.LIMIT_BAL), rjitt((dfcr01.BILL_AMT5+dfcr01.BILL_AMT6)/2),

           s=1,alpha=0.1)

plt.xlabel('LIMIT_BAL')

plt.ylabel('BILL_AMT 2M AVG')

plt.show()