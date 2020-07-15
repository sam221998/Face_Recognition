from facematch1 import x
#from facematch2 import x
from facematch1 import sentimg
#from facematch2 import sentimg
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

for i in wiki.select('table.infobox.biography.vcard'):
     m=i.getText()
     print(m)
    
for i in wiki.select('table.infobox.vcard'):
    n=i.getText()
    print(n)

j=cv2.imread('/home/sameer/project/sem2/images/'+sentimg)
cv2.imshow("Match image is ",j)
cv2.waitKey(0)
cv2.destroyAllWindows()
