import adafruit_dht 
import board
import os
import time
import requests

#dht = DHT22(board.D4)
dht = adafruit_dht.DHT22(board.D4, use_pulseio=False)
thingspeak_key = '932RYNZS3Z7NNRVO'

while True:
    try:
        humidity = dht.humidity      
        temperature = ((dht.temperature*(9/5)) + 32)
        temperature = round(temperature,1)
        print(temperature,"f ", humidity, "%")
                
        if humidity is None or temperature is None:
            f = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'status':'failed to get reading'})
        else:
            # Send the data to Thingspeak
            r = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'field1':temperature, 'field2':humidity})
            
    except:
        time.sleep(2)

dht.exit() 
        

