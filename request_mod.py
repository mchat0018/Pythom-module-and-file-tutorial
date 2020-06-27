import requests

#r=requests.get('https://xkcd.com/353/')
#print(r.text) prints the html contents of the site (unicode information)

payload={'page':2, 'count':5}
r= requests.get('https://httpbin.org/get',params=payload,timeout=5)   #pass the payloa as parameters to get router information
print(r.url)
print(r.text)

payload={'username':"Mihir",'password':"h5rt3@l"}
r= requests.post('https://httpbin.org/post',data=payload,timeout=5)   #post a form to a router
print(r.text)
r_dict=r.json()     #string returned is converted to dict
print(r_dict['form'])

r=requests.get('https://httpbin.org/basic-auth/mihir/testing',auth=('mihir','testing'),timeout=5) #responds to basic authentication
print(r)
print(r.text)