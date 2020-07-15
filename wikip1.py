
import sys
import requests
import bs4




st=str(input())
res=requests.get('https://en.wikipedia.org/wiki/'+st)
res.raise_for_status()
wiki=bs4.BeautifulSoup(res.text,"html.parser")
print("Name:")
for i in wiki.select('table.infobox.biography.vcard'):
     print(i.getText())

for i in wiki.select('table.infobox.vcard'):
     print(i.getText())


