import requests
from requests.exceptions import ConnectTimeout
import json



class Translate():
    headers = {'User-Agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}
    def __init__(self, word):
        self.word = word             #初始化单词

        
    def translate(self):      #用于发送请求,获取数据

        '''
        具体思路：
                 先去有道找到API接口,传入POST请求的参数，返回JSON数据，利用JSON库从中提取出翻译内容
        
        '''
        try:
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
            key = {
                'type':'AUTO',
                'i':self.word,            #需要翻译的单词或者句子
                'doctype':'json',
                'version':'2.1',
                'keyfrom':'fanyi.web',
                'ue':'UTF-8',
                'action':'FY_BY_CLICKBUTTON',
                'typoResult':'true'
                }                       
            response = requests.post(url=url, data=key, headers=self.headers)        #POST请求
            if response.status_code == 200:           
                self.get_word(response.text)
            else:
                print("请求失败，请重试")
        except ConnectTimeout as e:
            print('error: 请求超时')

        except Exception as e:
            print("Failure: ", str(e))

    def get_word(self, data):           #解析JSON数据
        if data:
            data = json.loads(data)
            if data:
                result = data.get('translateResult')
                src = result[0][0].get('src')
                tgt = result[0][0].get('tgt')
                print("翻译的单词或者句子为：", src)
                print("Translation results for:", tgt)
                print("Exit, please input n")
            else:
                print("返回的不是json数据格式的数据")
                
        else:
            pass

    def main(self):
        self.translate()


if __name__ == "__main__":
    while True:
        word = input("Please enter the need to translate words or sentences：")
        word = word.lower()
        if word != 'n':
            t = Translate(word)
            t.main()
        else:
            break
