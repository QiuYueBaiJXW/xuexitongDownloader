import requests
import sys

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987\
	    .116 Safari/537.36',
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
