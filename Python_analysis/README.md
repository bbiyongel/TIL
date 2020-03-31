
# Tips

분석 프로젝트 진행방안



목적: 교육중 학습 내용의 숙달 및 향후 업무활용을 위한 준비



주제: 자유 선정.

   -- 가능하면 금융업, 자사업무와 관련된 내용. 기존업무이외의 확장도 가능)

활용 데이터셋: 

  -- 교육중 활용했던 데이터 (신용카드, 보험, 주식시장) 또는 기타 업무유관 데이터셋

  -- 외부데이터 활용 가능 (구글트렌드, 네이버트렌드, 통계청, 소셜미디어 등)

범위: 총가용시간을 고려하여 한정

총가용시간: 2.5일 (사전 주제 선정 및 데이터 준비 권장)



산출물

  - 요약 보고서(10분 가량으로 프리젠테이션 가능한 분량 PPT 10장 내외 + 필요시 부록 추가)

  - 데이터 처리와 분석을 포함한 결과물을 담은 노트북 파일



주의사항:

  -- 매우 짧은 기간 동안 진행하는 프로젝트이므로 시간 배분 중요

  -- 주제선정과 사용데이터 선정에 과다한 시간 투입시 뒷단계 시간 부족 우려

  -- 필요한 모든 데이터를 확보하고 모든 다양한 분석을 시행하는 것은 불가능하므로

     평가 포인트와 프로젝트 수행 목적을 고려하여 범위를 조절할 것

  -- 팀단위 프로젝트 이므로 팀내의 원활한 업무 분장 및 협업, 참여

  

평가포인트: 

   [1] 교육중 습득한 데이터 처리 및 분석 방법론과 기술을 충분히 활용했는가? - 기술

        - 다양한 데이터 처리 방식을 활용했는가?
        - 다양한 데이터 분석 기법을 활용했는가?
        - 데이터 분석 결과가 완성도가 높은가?

   [2] 향후 업무에 활용시 유용할 방식으로 분석했는가? - 업무활용가능성

        + 다양한 데이터를 분석에 사용했는가?



   [3] 데이터 분석 과제를 참신한 시각으로 접근하여 흥미로운 결과를 도출했는가? - 문제해결 참신성



#########
프로젝트 결과 발표자료(PT) 구성 - 참조항목
#########
(분량: 10분 발표 기준 10장 내외 권장)

* 분석 주제의 내용과 범위 
  -- 범위에 무엇은 포함하지 않는가
  -- 왜 이 주제를 선택했는가
* 분석 주제의 업무 응용, 활용 가능성 - 시사점
  -- 본 프로젝트는 제약이 있지만 실제 업무에서는 어떤 방식이 가능하며
      유용할 것인가? 어떤 업무에서 어떤 데이터를 사용해서 어떻게 분석하면
      실제 기여가 될 것인가?
* 분석과정에서 파악된 흥미로운 패턴
  -- 상식이나 예상과 다른 주요 패턴 (found previously unknowns)
     예: 이 지역은 특이하게 상식적인 관계와 반대로 나타남
         특정 기간에는 일반적인 패턴이 나타나지 않음
         특정 영역에서만 상식적인 패턴이 집중되어 있음
         상식적으로 중요한 관계가 있다고 생각하는 변수간 관계 보다
         다른 변수들간의 관계가 더 강함
* 프로젝트 수행에서 느낀 점 (Lessons learned)
  -- 프로젝트에서 무엇을 배웠고 느꼈는가?
     예: 공공데이터 중 이런 부분은 활용가치 있음
         분석 방법에서 어떤 부분은 어떤 용도로 쓰면 좋겠음
         데이터 정제가 매우 중요 - 더 정밀한 무언가가 필요
         주제 선정과 문제 구체화, 최종 결과물의 명확한 정의가 초기에 중요







프로젝트를 위한 주제 - 데이터 설정 후보 - Example

--------------------------



[1] Credit Card Default Prediction 데이터셋을 사용하되 Default 대신

BILL_AMT6를 예측하는 모델을 개발

'default.payment.next.month'와 'PAY_AMT6', 'PAY_6' 등 

타겟으로 설정할 BILL_AMT6 와 동시점 또는 이후의 값을 사용가능한 변수에서

배제하고 그 이전 기간의 데이터들을 활용하여 사용액(청구)을 예측



[2] 기간별 추이로 업계와 관련된 공개된 데이터 활용

공공데이터포털에 공개된 도로교통공단_월별_주야별 교통사고 통계

( https://www.data.go.kr/dataset/3038489/fileData.do ) 데이터와 

구글트렌드의 교통사고와 잠재적인 관계가 있을 것으로 예상되는 데이터를

결합하여 익월의 교통사고 건수, 사망자수, 부상자수를 예측하는 모델을 개발



[3] 미세먼지와 신용카드 사용액 추이간의 관계를 통한 신용카드 사용액 예측 모델 개발

신용카드 통계 (http://kosis.kr/search/search.do?query=%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C )

미세먼지 통계 ( http://kosis.kr/search/search.do?query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80 )

기타 추가 가능한 데이터 결합



[4] 규모가 큰 (증권) 종목 (예: 삼성전자, 현대차, 네이버 등) 5개 정도의 미래 시가총액을

예측하는 모델을 개발. 외부통계로부터 미국주식시장, 환율, 국내경제통계 등을 결합하여

예측모델 생성





****---------------------

github : 

https://github.com/stillxyxon/py_ml_analysis 







########## DT를 위한 세팅



import pydotplus

import graphviz



import os

os.environ["PATH"] += os.pathsep + 'C:\\Users\\user\\Anaconda3\\Library\\bin\graphviz'



순서:

Anaconda 관리자모드로 실행

conda install pydotplus

conda install graphviz



스크립트에서 os path 추가 부분 재지정 (path 모르면 graphviz 검색 ) 


조치 >> 
https://livetoday.tistory.com/entry/graphviz-%EC%84%A4%EC%B9%98-%ED%9B%84-%EC%98%A4%EB%A5%98-Anaconda

셀을 하나 추가한 후 pip install 사용해서 >>

! pip install graphviz

! pip install graphviz



실행





anaconda pompt를 실행시킨 후 

conda install graphviz

명령을 실행하면 graphviz 설치

완료되면 promplt에서 exit













X = dfc20[['amt_pstyr']]

# 독립변수의 리스트로 정의. 

# 하지만, 내용물은 하나 뿐이기에 단순선형회귀분석

Y = dfc20['amt_nxtyr']

 

# with sklearn

regr = linear_model.LinearRegression()

regr.fit(X, Y)



print('Intercept:  ', regr.intercept_)

print('Coefficients:  ', regr.coef_[0]) 

# 리스트이기 때문에 0번 요소를 출력해야 숫자



# make predictions - back test

predictions = regr.predict(X)



# scatter plot 그리기

plt.scatter(rjitt(dfc20.amt_pstyr), rjitt(dfc20.amt_nxtyr),

            color='blue', s=2, alpha=0.1)

plt.plot([0,dfc20.amt_pstyr.max()],[0,dfc20.amt_pstyr.max()], 

         color='grey', linestyle=':')

plt.plot(X,predictions, color='red', linestyle=':')

plt.xlabel('past year')

plt.ylabel('next year')

plt.title('AMT Change Pattern')

plt.show()







[연습문제] 스타벅스 2만원~4만원 구간만을 가지고 내년이용건수와의 scatterplot을 작성하라



dfctmp = dfc20.copy()

dfctmp = dfctmp[(dfctmp.amt_strbk>=20000) & (dfctmp.amt_strbk<=40000)]



plt.scatter(rjitt(dfctmp.amt_strbk), rjitt(dfctmp.cnt_nxtyr), 

            alpha=0.1, s=5)

plt.xlabel('amt_strbk')

plt.ylabel('cnt_nxtyr')

plt.show()



## Keras 설치

https://pyther.tistory.com/17



클러스터링 >> 요약 버전



dfcc05 = dfcc01[['amt_nike', 'amt_strbk']]

# create k-means model

kmm1 = KMeans(n_clusters=5, random_state=111)  

kmm1.fit(dfcc05)  



X1 = dfcc05.copy()

X1['clst'] = kmm1.labels_ 



df_clstprfl = X1.groupby('clst').mean().reset_index() 

df_clstprfl







#----------------------



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





#---------------

프로젝트를 위한 주제 - 데이터 설정 후보 - Example

--------------------------



[1] Credit Card Default Prediction 데이터셋을 사용하되 Default 대신

BILL_AMT6를 예측하는 모델을 개발

'default.payment.next.month'와 'PAY_AMT6', 'PAY_6' 등 

타겟으로 설정할 BILL_AMT6 와 동시점 또는 이후의 값을 사용가능한 변수에서

배제하고 그 이전 기간의 데이터들을 활용하여 사용액(청구)을 예측



[2] 기간별 추이로 업계와 관련된 공개된 데이터 활용

공공데이터포털에 공개된 도로교통공단_월별_주야별 교통사고 통계

( https://www.data.go.kr/dataset/3038489/fileData.do ) 데이터와 

구글트렌드의 교통사고와 잠재적인 관계가 있을 것으로 예상되는 데이터를

결합하여 익월의 교통사고 건수, 사망자수, 부상자수를 예측하는 모델을 개발



[3] 미세먼지와 신용카드 사용액 추이간의 관계를 통한 신용카드 사용액 예측 모델 개발

신용카드 통계 (http://kosis.kr/search/search.do?query=%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C )

미세먼지 통계 ( http://kosis.kr/search/search.do?query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80 )

기타 추가 가능한 데이터 결합



[4] 규모가 큰 (증권) 종목 (예: 삼성전자, 현대차, 네이버 등) 5개 정도의 미래 시가총액을

예측하는 모델을 개발. 외부통계로부터 미국주식시장, 환율, 국내경제통계 등을 결합하여

예측모델 생성





#################

# Q & A in Project



S&P 500 구성 종목의 분류 체계 (health care, IT ,.... )

https://en.wikipedia.org/wiki/List_of_S%26P_500_companies 



무작위 값 생성 참고 스크립트 (링크)

 >> 함수 실행하고 함수를 통해서 생성

https://stackoverflow.com/questions/50626710/generating-random-numbers-with-predefined-mean-std-min-and-max?fbclid=IwAR0I4SkjbQWH2_cJyAwaTtW5l-QUnr8npvb5XRHQz0OOkWAp5xd6yzCDGn0



# rndn은 정규분포를 따르는 무작위 값을 생성

# 정규분포여부는 hist 명령으로 시각적으로 확인 가능

# Visual Normality Checks
# histogram plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# histogram plot
pyplot.hist(data)
pyplot.show()




크롤링에서 .... 띄어쓰기 한칸 제거



def get_url(item_name, code_df):



    # 코드를 가져오기 위한 처리.

    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index = False)



    # url은 일일 종가 시가 고가 저가 거래량을 보여주는 표

    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code = code)

    url = url.replace(" ","") # 한줄 추가해서 스페이스 들어간 것을 제거

    print("요청 URL = {}".format(url))

    return url







구글트렌드를 이용한 나이키-아디다스 브랜드 매출 예측 예제

https://github.com/stillxyxon/SSF_prj  





# 한글이 챠트에서 제대로 표시되도록 설정



import matplotlib.font_manager as fm



fm.get_fontconfig_fonts()

# For Windows

font_name = fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()

print(font_name)

plt.rc('font', family=font_name)



plt.rcParams['axes.unicode_minus'] = False #  음수를 나타내는 '-' 부호가 정상 표시되도록








import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

from numpy.polynomial.polynomial import polyfit

import matplotlib.style as style 

from IPython.display import Image



import warnings

warnings.filterwarnings('ignore')



# define random jitter

def rjitt(arr):

    stdev = .01*(max(arr)-min(arr))

    return arr + np.random.randn(len(arr)) * stdev





박스플롯 그리기

# Create the boxplot

plt.boxplot([d11.nikerv, d11.adidasrv])

plt.xticks([1, 2], ['nike', 'adidas'])

plt.title('revenue distibution')

plt.show()





네트워크분석 예제 :: 

https://intelligentonlinetools.com/blog/2018/02/10/how-to-create-data-visualization-for-association-rules-in-data-mining/

axis 

iloc

[:, 1]   # 행 : 모든행 , 종 : 2번째부터


feature importance shap value

xgboost.plot_importance



import shap
import skimage

skimage.__version__


shap.initjs()
shap.force_plot(explainer.expeted_value, shap_values[0,:], test_x,iloc[1,:])

shap.force_plot(explainer.expeted_value, shap_values, test_x)


shap.summary_plot(shap_values,test_x)

shap.summary(shap_values, test_x, plot_type="bar")


shap.dependence_plot("grade", shap_values, test_x)


https://github.com/slundberg/shap 


