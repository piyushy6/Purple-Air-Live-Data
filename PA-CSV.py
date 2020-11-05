import requests
from pandas import json_normalize
from time import sleep
import datetime 
import pandas as pd

def logfilename():
    now = datetime.datetime.now()
    return 'PA_Data_%0.4d-%0.2d-%0.2d_%0.2d-%0.2d-%0.2d.csv' % \
                (now.year, now.month, now.day,
                 now.hour, now.minute, now.second)

filename=logfilename()

while True: 
   url = "http://172.20.10.2/json?live=true"
   # (where Sensor IP Address on the Local Network is the IP address assigned by your router to the sensor, so you will have to replace it according to the IP address assigned to your sensor in the above URL)
    
   PA_Data = requests.get(url=url)
   
 # To convert JSON data to dataframe type
   df = json_normalize(PA_Data.json())

 # To correct the format of UTC Time
   df['DateTime']= pd.to_datetime(df['DateTime'], format='%Y/%m/%dT%H:%M:%SZ')

 # To add IST in the dataframe
   df['IST-Time']= datetime.datetime.now().strftime("%H:%M:%S")
 # df['IST-Date-Time']= datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
   
 #  print(df)
   print(df[['IST-Time','pm2_5_atm_b','pm2_5_atm']].to_string(index=False))

   # Sampling Time 
   sleep(5)

   # Storing Data in CSV File
   with open(filename, 'a') as f:
  #  df.to_csv(f, header=f.tell()==0,index=False) -> To store entire sensor data

    df_reorder = df[['DateTime','IST-Time','pm2_5_atm_b','pm2_5_atm','pm2.5_aqi_b','pm2.5_aqi','pm2_5_cf_1_b','pm2_5_cf_1','pm1_0_atm_b','pm1_0_atm','pm1_0_cf_1_b','pm1_0_cf_1','pm10_0_atm_b','pm10_0_atm','pm10_0_cf_1_b','pm10_0_cf_1','current_temp_f','current_humidity','current_dewpoint_f','pressure']]
    df_reorder.to_csv(f, header=f.tell()==0,index=False)
#  header=f.tell()==0) -->> "Add header if file is being created, otherwise skip it"

