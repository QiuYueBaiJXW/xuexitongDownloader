import requests
import sys

headers = {
  
}
objid = sys.argv[1]
type = sys.argv[2] 
baseurl = 'http://d0.ananas.chaoxing.com/download/'
url = baseurl + objid
print(url)
savepath = './'
if type == "1":
	r = requests.get(url,headers=headers)
	with open('./' + "1.pdf",'wb+') as f:
		f.write(r.content)
else:
	r = requests.get(url,headers=headers)
	with open('./' + "1.flv",'wb+') as f:
		f.write(r.content) 
