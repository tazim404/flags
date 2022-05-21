from bs4 import BeautifulSoup
import requests
file=open("./sayches.html",'r')
html=file.read()

soup=BeautifulSoup(html,'html.parser')
options=soup.find_all('option')
for option in options:
    country_code=option['value'].lower()
    country_image=requests.get(f"https://cdn.sayches.com/assets/images/flags/{country_code}.png")
    with open(f"images/{country_code}.png","wb") as file:
        file.write(country_image.content)
        print("Downloaded",option.text)
