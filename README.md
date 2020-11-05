# Purple-Air-Live-Data
This script helps to access and store the Real-Time data of Purple Air sensor. 

There are currently 2 ways to get access to Purple Air Sensor data, 

a.) By downloading it from the website (https://www.purpleair.com/map)  

b.) Getting access to the data from the onbaord SD-Card.

The issue with these methods is, the Purple Air sensor uses ESP8266 chip. The code for getting the data from sensor in ESP8266 has a sampling rate of 120 seconds (2 minutes).
Thus we can only access the data of 2 minutes average of the sensor. (The data is the average of 2 PMS5003 Plantower sensor onboard)

This makes the sensor not that suitbale for mobile sening applications where we require highly temporal data to get fine-grained spatio-temporal data.

Thus, this script helps to get real-time data of the purple air sensor. This will make the sensor extremely suitable for mobile sensing applications like- Cars, Public Buses or Drones.

Storing the JSON Data from the sensor : 

By using this script, we can access the purple air sensor data in a JSON format locally using the IP address or hostname of the sensor and store it in a CSV file.

The URL to get the live sensor data:

http:// Sensor IP Address on the Local Network or Hostname/json?live=true
  
(where Sensor IP Address on the Local Network is the IP address assigned by your router to the sensor)

In order to store the Json data in CSV file, we first Normalize the JSON data into a flat table. We then save this dataframe to CSV file.
