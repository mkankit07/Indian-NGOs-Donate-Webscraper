import requests ,json
from bs4 import BeautifulSoup
from pprint import pprint
url="https://www.giveindia.org/certified-indian-ngos"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
aa=soup.find("div",class_="d-flex f-d-col w-100 p-0 container")
dd=aa.find_all("h5")
ss=aa.find_all("span")
list1=[]
for i,j in zip(dd,ss):
    dict1={}
    kk=((j.text).split("|"))
    dict1["name"],dict1["cause"],dict1["state"]=i.text,kk[0].replace(" ",""),kk[1].replace(" ","")
    list1.append(dict1)
pprint(list1)
# a=input("Enter the cause/state \n")
# for j in list1:
#     if a ==j["state"] or a==j["cause"]:
#         print(j["name"])
r=open("user.json","w")
json.dump(list1,r,indent=4)
