import os
import urllib.request
import urllib.parse
import json
import time
while  True:
    content=input('输入翻译内容（输入&&&退出程序）:')
    if content=='&&&':
        break

    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    data={}
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']= 'dict'
    data['client:']='fanyideskweb'
    data['salt']='15965290351827'
    data['sign']='d351408d47975ffb11bbbf82a4eec754'
    data['ts']='1596529035182'
    data['bv']='7b07590bbf1761eedb1ff6dbfac3c1f0'
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_REALTlME'

    data=urllib.parse.urlencode(data).encode('utf-8')
    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')
     
    target=json.loads(html)
    print('翻译结果:%s'%(target['translateResult'][0][0]['tgt']))

    #time.sleep(1)

    #os.system('pause')
     
