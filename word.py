import http.client
import hashlib
import urllib.parse
import random
def search_word(word):
    appKey = '056d09a69c28c55d'
    secretKey = 'YaiCmJ7AdhkJX9fjBmX10wSyhFvDhbWS'

     
    httpClient = None
    myurl = '/api'
    q = word
    fromLang = 'EN'
    toLang = 'zh-CHS'
    salt = random.randint(1, 65536)

    sign = appKey+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appKey='+appKey+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
     
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
     
        response = httpClient.getresponse()
        a=response.read().decode()
        #print(a)
        return a
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

def conduct(a):
    exp_list=[]
    a=eval(a)
    b=a['web']
    c=a['basic']
    num=0
    for i in b:
        exec('explain_'+str(num)+ "=[i['key'],i['value']]")
        exp_list.append(eval('explain_'+str(num)))
        num+=1
    detail=c['explains']
    ph=c['us-phonetic']
    outlist=[ph,detail,exp_list]
    return outlist

if __name__=='__main__':
    a=input()
    b=search_word(a)
    c=conduct(b)
##    print(a)
##    print(c)
