# pip install request 
import requests

url = "https://www.onlinekhabar.com/smtm/home/trending"

r = requests.get(url=url)
if r.status_code==200:
    print(r.json())
else:
    print("something went wrong")