import requests
import json
from datetime import date 
import time

while True:
    response = requests.get("http://3.88.31.90:82/testapi/wdrest.svc/GetAWSDataAPI_V2/2021-01-13/"+str(date.today())+"/862549045430298/DeviceDate")
    file1 = open("response.txt","w") 
    file1.write(response.text) 
    file1.close()
    time.sleep(300)
# js = response.json()

# df = pd.read_json(js)
# df.to_csv("response.csv",index=False)
# print(response.text)
