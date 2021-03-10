# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import ast
import json
import rsa
import base64
import urllib.parse
import math

kb_global = {'1':'1'}

def jsooo(t):
  return json.loads(t)

def get_csrftoken (tt):

  bs_text = BeautifulSoup(tt.content,'lxml')
  csrftoken = bs_text.find_all('input')[7].get('value')
  return csrftoken


def get_t_ms():
  t =time.time()
  t_ms = int(round(t*1000))
  return str(t_ms)

def get_key(mod,exp):
  mod = base64.b64decode(mod).hex()
  exp = base64.b64decode(exp).hex()
  key = rsa.PublicKey(int(mod,16),int(exp,16))
  return key

def dec_rsa (password,key):
  b16 = rsa.encrypt(bytes(password.encode('utf-8')),key)
  str64 = str(base64.b64encode(b16),'utf-8')
  return str64

def main(term = '2020,1'):
  use_id = "1902053119"
  use_password = "19990923xx"

  url_home = "http://218.204.129.252:8088/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t={0}"#登入界网址
  url_approve = "http://218.204.129.252:8088/jwglxt/xtgl/login_slogin.html?time={0}"#认证网址
  url_key = "http://218.204.129.252:8088/jwglxt/xtgl/login_getPublicKey.html?time={0}"#mod exp 获取
  url_Schedule = "http://218.204.129.252:8088/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N253508 "#课表网址
  

  headers_key = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': '',#
  'DNT': '1',
  'Host': '218.204.129.252:8088',
  'Referer': '',#
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
  'X-Requested-With': 'XMLHttpRequest'
  }

  headers_Schedule = {
    'Host': '218.204.129.252:8088',
    'Proxy-Connection': 'keep-alive',
    'Content-Length': '14',
    'Accept': '*/*',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'http://218.204.129.252:8088',
    'Referer': 'http://218.204.129.252:8088/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?gnmkdm=N253508&layout=default&su=1902053119',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': ''
  }

  headers_approve = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '',#
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '',#
    'DNT': '1',
    'Host': '218.204.129.252:8088',
    'Origin': 'http://218.204.129.252:8088',
    'Referer': '',#
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
  }


  font = {
    'csrftoken': "",
    'yhm': "",
    'mm': "",
  }


  #获取模数和指数 算出公钥
  re = requests.Session()
  new_url = url_home.format(get_t_ms())

  new_text = re.get(new_url)
  cookies = requests.utils.dict_from_cookiejar(re.cookies)
  route = '; route='+cookies['route']
  cookies = 'JSESSIONID='+cookies['JSESSIONID']+'; route='+cookies['route']
  
  headers_key['Referer'] = new_url
  headers_key['Cookie'] = cookies

  mod_exp = jsooo(re.get(url_key.format(get_t_ms()), headers= headers_key).text)
  key = get_key(mod_exp['modulus'],mod_exp['exponent'])

  font['csrftoken'] = urllib.parse.quote(get_csrftoken(new_text))
  font['yhm'] = urllib.parse.quote(use_id)
  font['mm'] = urllib.parse.quote(dec_rsa(use_password,key))

  data_data = 'csrftoken='+font['csrftoken'] +"&"+'yhm='+font['yhm']+"&"+'mm='+font['mm']+"&"+'mm='+font['mm']

  conten_length = len('csrftoken='+font['csrftoken'])+len('yhm='+font['yhm'])+len('mm='+font['mm'])*2+3

  headers_approve['Referer'] = new_url
  headers_approve['Cookie'] = cookies
  headers_approve['Content-Length'] = str(conten_length)

  new_url = url_approve.format(get_t_ms())
  text_context = re.post(new_url, headers = headers_approve, data = data_data, allow_redirects=False)
  cookies = requests.utils.dict_from_cookiejar(text_context.cookies)
  print(cookies)
  print(text_context.text)
  cookies = 'JSESSIONID='+cookies['JSESSIONID'] + route

  headers_Schedule['Cookie'] = cookies
  a,b = term.split(',')
  if b == '1' :
    b = '3'
  else:
    b = '12'
  term = 'xnm='+a+'&xqm='+b
  schedule = re.post(url_Schedule, headers = headers_Schedule, data = term)
  json_data = jsooo(schedule.text)
  kb_global = data_clear(json_data)
  return kb_global
  

def data_clear(t):
  kb = {
    '星期一':{'1-2':[],"3-4":[],"5-6":[],"7-8":[],"9-10":[],},
    '星期二':{'1-2':[],"3-4":[],"5-6":[],"7-8":[],"9-10":[],},
    '星期三':{'1-2':[],"3-4":[],"5-6":[],"7-8":[],"9-10":[],},
    '星期四':{'1-2':[],"3-4":[],"5-6":[],"7-8":[],"9-10":[],},
    '星期五':{'1-2':[],"3-4":[],"5-6":[],"7-8":[],"9-10":[],},
    '星期六':{'1-2':[],"3-4":[],"5-6":[],"7-8":[],"9-10":[],},
    '星期天':{'1-2':[],"3-4":[],"5-6":[],"7-8":[],"9-10":[],},
    }
  for a in t['kbList']:
    Place_or_Single_Or_Double_or_Cycle = []

    if '(' in a['zcd']:
      new = a['zcd'][:-4].partition('-')
      Place_or_Single_Or_Double_or_Cycle = [a['kcmc'], a['cdmc'], a['zcd'][-2:-1], new[0], new[2]]
    else:
      new = a['zcd'][:-1].partition('-')
      Place_or_Single_Or_Double_or_Cycle = [a['kcmc'], a['cdmc'], '全', new[0], new[2]]

    kb[a['xqjmc']][a['jc'][:-1]].append(Place_or_Single_Or_Double_or_Cycle)
    

  return kb

def find_schedule(index_kb,kb):
  a,b = index_kb.split(',')
  b = math.ceil(int(b)/2)-1
  result = ''
  index_date = {
    '1':'星期一',
    '2':'星期二',
    '3':'星期三',
    '4':'星期四',
    '5':'星期五',
    '6':'星期六',
    '7':'星期天',
  }
  time_schedule = {
    '1':"08:20",
    '2':"10:15",
    '3':"14:00",
    '4':"15:55",
  }
  i = 0
  for key_kb in kb[index_date[a]]:
    print(key_kb)
    if i == b :
      result = kb[index_date[a]][key_kb]
      break
    i = i + 1
  result = result if len(result) !=0 else [["无课","无课"],["无课","无课"]]
  return result,time_schedule[str(i+1)]

if __name__ == "__main__":
  kb_global = main()
  aa = find_schedule('2,3',kb_global)
  print(aa)
  pass
