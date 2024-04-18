import requests
from bs4 import BeautifulSoup
import pandas as pd
#the number of the website is written at the last letter of the URL 
url="https://yoursite.com/page=1"
response=requests.get(url)
a=response.text
soup = BeautifulSoup(response.content, 'html.parser')
h2="name of the class in the html tag"
div="name of the class in the html tag"
#specified data to be downloaded
name=[]
address=[]
#number of pages
n=21
if response.status_code==200:
    for i in range(n):
        url=url[:-1]+str(int(url[-1])+1)
        response=requests.get(url)
        a=response.text
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all("div",attrs={"class":"name of the class"})
        names=soup.find_all("h2",attrs={"class":"name of the class"})
        for i in titles:
            address.append(i.text)
        for j in names:
            name.append(j.text)
else:
    print("port error")
df=pd.DataFrame(name)
df1=pd.DataFrame(address)
Df_8=pd.concat([df,df1],axis=1)
csv_data=Df_8.to_excel("data.xlsx",index=False)


