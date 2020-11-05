import requests
from pandas import json_normalize
from time import sleep
import datetime


def logfilename():
    now = datetime.datetime.now()
    return 'PA_Data_%0.4d-%0.2d-%0.2d_%0.2d-%0.2d-%0.2d.csv' % \
                (now.year, now.month, now.day,
                 now.hour, now.minute, now.second)

filename=logfilename()

while True: 
   url = "http://172.20.10.2/json?live=true"
   PA_Data = requests.get(url=url)
   
  # To convert JSON data to dataframe type
 
   df = json_normalize(PA_Data.json())
   print(df)
   
   # Sampling Time 
   sleep(5)

   # Storing Data in CSV File
   with open(filename, 'a') as f:
    df.to_csv(f, header=f.tell()==0,index=False)
#  header=f.tell()==0) -->> "Add header if file is being created, otherwise skip it"

