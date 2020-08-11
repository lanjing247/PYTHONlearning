import urllib.request
import urllib.parse
import json

while  True:
    TranslationContent=input('输入翻译内容（输入&&&退出程序）:')
    if TranslationContent=='&&&':
        break

    YouDaoFanYiUrl='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    FormData={}
    FormData['i']=TranslationContent
    FormData['from']='AUTO'
    FormData['to']='AUTO'
    FormData['smartresult']= 'dict'
    FormData['client:']='fanyideskweb'
    FormData['salt']='15965290351827'
    FormData['sign']='d351408d47975ffb11bbbf82a4eec754'
    FormData['ts']='1596529035182'
    FormData['bv']='7b07590bbf1761eedb1ff6dbfac3c1f0'
    FormData['doctype']= 'json'
    FormData['version']= '2.1'
    FormData['keyfrom']= 'fanyi.web'
    FormData['action']= 'FY_BY_REALTlME'

    ResponseFormData=urllib.parse.urlencode(FormData).encode('utf-8')
    Response=urllib.request.urlopen(YouDaoFanYiUrl,ResponseFormData)
    Html=Response.read().decode('utf-8')
     
    Target=json.loads(Html)
    print('翻译结果:%s'%(Target['translateResult'][0][0]['tgt']))

