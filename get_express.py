import requests

def get_data(number)
# express_name='yuantong'
# number='YT5131449647466'
url='https://www.kuaidi100.com/query?'
params = {
          'type': express_name,
          'postid': number,
          'temp': '0.9661515218223198',
          'phone':''
          }
res=requests.get(url,params=params)
result=res.json()
print(result)
