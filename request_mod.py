import requests

#r=requests.get('https://xkcd.com/353/')
#print(r.text) prints the html contents of the site (unicode information)

r= requests.get('https://imgs.xkcd.com/comics/python.png')

print(r.status_code) 
#200 is a success
#300 is redirect
#400 is a client-error
#500 is a server error
print(r.ok) #will return True for anything that is less than a 400 response
print(r.headers)    #return type=dict
