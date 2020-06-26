import requests

#r=requests.get('https://xkcd.com/353/')
#print(r.text) prints the html contents of the site (unicode information)

r1= requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png','wb') as f:
    f.write(r1.content)  #writes binary information to the .png file

