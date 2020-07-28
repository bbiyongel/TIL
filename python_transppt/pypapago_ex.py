from pypapago import Translator

translator = Translator()

result = translator.translate('I am GROOT')
print(result) # 나는 그루트다



from pypapago import Translator

translator = Translator()

result = translator.translate(
    '카카오는 파파고를 좋아해',
    source='ko',
    target='en',
)
print(result) # Kakao likes papago.




#Code	Desc
#ko	Korean
#en	English
#ja	Japanese
#zh-CN	Chinese
#zh-TW	Chinese traditional
#es	Spanish
#fr	French
#vi	Vietnamese
#th	Thai
#id	Indonesia