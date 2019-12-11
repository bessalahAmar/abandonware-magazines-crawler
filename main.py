import requests
from bs4 import BeautifulSoup


mylist = []
listDownload = []

#page = 1 ... 15
for i in range(1,16,1):
    s = "https://www.abandonware-magazines.org/affiche_mag.php?mag=404&page="+str(i)
    r = requests.get(s)
    soup = BeautifulSoup(r.text,"html.parser" )
    for a in soup.find_all('a', href=True):
        if a['href'].startswith("download"):
            mylist.append("https://www.abandonware-magazines.org/"+a['href'])
    mylist = list(dict.fromkeys(mylist))

f = open("listLien.txt", "a")

for url in mylist :
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser" )
    for a in soup.find_all('a', href=True):
        #print(a['href'])
        if "download.abandonware.org" in a['href']:
            print(a['href'])
            f.write(a['href'])
    	     #filename = wget.download(a['href'])
f.close()
            
    



