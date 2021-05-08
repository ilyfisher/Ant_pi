import adafruit_dht 
import board
import os
import time
import requests

#dht = DHT22(board.D4)
dht = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
    try:
        temperature, humidity = dht.temperature, dht.humidity
        print(temperature, humidity)
        
        # If either reading has failed after repeated retries,
        # abort and log message to ThingSpeak
        thingspeak_key = '932RYNZS3Z7NNRVO'
        if humidity is None or temperature is None:
            f = requests.post('https://api.thingspeak.com/update.json', data = {'932RYNZS3Z7NNRVO':thingspeak_key, 'status':'failed to get reading'})
        else:
            # Send the data to Thingspeak
            r = requests.post('https://api.thingspeak.com/update.json', data = {'932RYNZS3Z7NNRVO':thingspeak_key, 'field1':temperature, 'field2':humidity})
    
    except:
        time.sleep(2)

dht.exit() 
        

