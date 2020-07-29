$ pip install pandas   #pandas 패키지
$ pip install xlrd     #pandas에서 엑셀파일 관련 패키지 
$ pip install --upgrade google-cloud-translate #google 번역기 api 패키지


import os
# 구글 번역 api 인증 키 파일 설정
# 다운로드한 json파일 위치를 넣어주면 된다.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\\Project-11111111.json'

# 환경변수 확인해보기
print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
# 구글 클라우드 번역 라이브러리 
from google.cloud import translate

# 번역 함수 
def trans(text, target = 'ko'):
    # 클래스 생성 
    translate_client = translate.Client()
    # 번역 시작
    translation = translate_client.translate(
        text,
        target_language=target)

    # 번역전 문자열 
    print(u'Text: {}'.format(text))
    # 번역후 문자열
    print(u'Translation: {}'.format(translation['translatedText']))
    # 번역한 문자열 리턴
    return translation['translatedText']
#pandas 라이브러리
import pandas as pd

# d:\\ch.xlsx파일을 불러온다.

data = pd.read_excel('D:\\ch.xlsx', index_col=None, header=None)
# 데이터 행수 화면에 표시
print(data.index)
# 데이터 행수 만큼 루프 
for row in data.index:
    #행의 1번째(0부터 시작) 문자열을 공백 제거후 읽어온다.  
    chText = str(data.loc[row, 1]).strip()    
    # 문자열에 데이터가 없다면 
    if chText != 'nan':
        # 문자열 출력
        print(data.loc[row,1])
        # 문자열을 번역함수로 전달 후 trans_text로 번역된 문자열을 리턴 받는다.
        trans_text = trans(chText)
        # 동일한 위치에 덮어 씌운다.
        data.loc[row,1] = trans_text

#이렇게 만들어진 데이터를 
#trans_to.xlsx파일로 저장한다.
data.to_excel('D:\\trans_to.xlsx')


