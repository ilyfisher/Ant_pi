  
import adafruit_dht 
import board
import os
import time
import requests

#dht = DHT22(board.D4)
dht = adafruit_dht.DHT22(board.D4, use_pulseio=False)
thingspeak_key = 'Your Write API Key Goes Here'

while True:
    try:
        humidity = dht.humidity      
        temperature = ((dht.temperature*(9/5)) + 32)
        temperature = round(temperature,1)
        print(temperature,"f ", humidity, "%")
                
        if humidity is None or temperature is None:
            f = requests.post('https://api.thingspeak.com/update.json', data = $
        else:
            # Send the data to Thingspeak
            r = requests.post('https://api.thingspeak.com/update.json', data = $
            
    except:
        time.sleep(2)

dht.exit() 
