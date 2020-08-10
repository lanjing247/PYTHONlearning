#  有道翻译爬虫介绍
##  URL

获取URL
```Python 
 url='http://fanyi.youdao.com/translate?smartresult=dictsmartresult=rule'
```
##  Form Data
在有道翻译页面检查元素之后，将Form Data内容写成字典形式。
```python

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
    ```

