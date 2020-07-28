#translate_ppt.py에서 참조 

import os
import sys
import json
import urllib.request

#개발자센터에서 발급받은 파파고 NMT API Client ID와 Client Secret 값
translate_client_id = "Sij4JRG_sI8ToMP2EKIf" 
translate_client_secret = "YP5pbrijbq"

#개발자센터에서 발급받은 언어감지 Client ID와 Client Secret 값
check_language_client_id = "m5mBFEdqUF8bfm3W53Yt"
check_language_client_secret = "gR9TBbUZ_K"

#언어 구분
def check_language(txt):
    #문자열을 url용으로 인코딩
    encQuery = urllib.parse.quote(txt)    
    data = "query=" + encQuery

    # 언어 감지 주소
    url = "https://openapi.naver.com/v1/papago/detectLangs"

    # 인증 정보 추가
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",check_language_client_id)
    request.add_header("X-Naver-Client-Secret",check_language_client_secret)
    try:
        # api 요청!
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        # 결과 코드 받기
        rescode = response.getcode()
        # 성공이면(200)
        if(rescode==200):
            #json형태로 변경하고
            response_body = json.loads(response.read())
            #langCode 항목을 가져옴 이 값으로 언어를 구분함.
            language = response_body['langCode']
            return language
        else:
            print("Error Code:" + rescode)            
    except urllib.error.HTTPError as e:
        #예외 처리!
        print(e.code)
        print(e.read())
    return None

'''
번역 함수
txt : 번역할 문자열
src_lang : 번역할 문자열 언어
tgt_lang : 번역을 요청할 언어
'''

def translate(txt, src_lang, tgt_lang):
    encText = urllib.parse.quote(txt)
    data = "source=" + src_lang + "&target=" + tgt_lang + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",translate_client_id)
    request.add_header("X-Naver-Client-Secret",translate_client_secret)
    try:
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            #json 형태
            response_body = json.loads(response.read())
            # message > result > translateText가 번역된 문자열
            trans_text = response_body['message']['result']['translatedText']
            # 번역된 문자열 리턴
            return trans_text        
        else:
            print("Error Code:" + rescode)
    except urllib.error.HTTPError as e:
        #예외 처리
        print(e.code)
        print(e.read())        
    return None

if __name__ == "__main__":    
    txt = 'ハードウェア機能要件'
    #언어 체크
    lang = check_language(txt)
    if lang is not None:
        #언어가 확인이 되었다면
        #해당 언어를 한국어로 번역해서 출력!
        print(translate(txt, lang, 'ko')) 