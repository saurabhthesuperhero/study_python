# 네이버 Papago NMT API 예제
import os
import sys
import json
import pprint
import urllib.request
client_id = "6LGVisW5NEklat6D8c2n"
client_secret = "Or2EuREJbK"
encText = urllib.parse.quote("퇴사하고 싶다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))

    jsonResponse = json.loads(response_body.decode('utf-8'))
    pprint.pprint(jsonResponse)
    print(jsonResponse['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)