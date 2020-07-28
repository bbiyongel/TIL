'''
파파고를 이용한 파일 내용 자동번역 코드
made by 안산드레이아스

설치파일
pip install pypapago
'''

from pypapago import Translator

# 불러올 파일명 입력(동일 디렉터리 위치)
fileName = './test.txt'

# 객체 할당, 번역할 파일 열기
translator = Translator()
with open(fileName, encoding='utf-8', errors='ignore') as f:
# 줄을 읽어 저장, byte를 string으로 디코딩
line = f.readline()
print(line) # 파일 내 텍스트 출력
print(type(line)) # 텍스트 타입 출력

# 번역할 문자를 입력
forTranslateString = line

# 번역하기 (\n(엔터) 이나오면 오류 발생 문자열 처리 필요) english -> korean 옵션
result = translator.translate(forTranslateString, source='en', target='ko', verbose=False)

# 결과 출력
print(result) # 번역된 텍스트 출력
with open("afterTranslate.txt", 'w') as f: # 번역 완료된 텍스트 저장
f.write(result)