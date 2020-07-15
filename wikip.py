from facematch2 import x
from facematch2 import sentimg
import sys
import requests
import bs4
import cv2

a=list(x)
b=a[0]

#st=str(input())
res=requests.get('https://en.wikipedia.org/wiki/'+str(b))
res.raise_for_status()
wiki=bs4.BeautifulSoup(res.text,"html.parser")

f=open('helloworld1.html','a')
message='<html><body><img src="/home/sameer/project/sem2/images/'+sentimg+'"></body></html>'
f.write(message)
f.close()

for i in wiki.select('table.infobox.biography.vcard'):
     m=i.getText()
     encoded_string = m.encode("ascii", "ignore")
     decode_string = encoded_string.decode()

     f = open('helloworld1.html','a')
     message = '<html><body><p>'+decode_string+'</p></body></html>'
     f.write(message)
     f.close()


for i in wiki.select('table.infobox.vcard'):
    n=i.getText()
    encstr = n.encode("ascii", "ignore")
    dstr = encstr.decode()

    f = open('helloworld1.html','a')
    message1= '<html><body><p>'+dstr+'</p></body></html>'
    f.write(message1)
    f.close()




