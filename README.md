# Ant_pi
Code to set up live cam, humidity, and temperature checker

## Writeup
[List of supplies]
•	Raspberry pi 3/power supply here 
•	Monitor, Mouse and Keyboard
•	USB to Micro SD card reader here
•	Raspberry pi case here 
•	Raspberry pi camera here 
•	Breadboard Jumper Wires here- only get these of the ones provided with the AM2303 are too short for your project
•	Heat Shrink Tubing here
•	AM2302 Temperature & Humidity Sensor here
[To make the Live video Feed]
1.	First set up your raspberry pi. I used a raspberry PI 3. 
•	Download raspberry pi imager using
	sudo apt install rpi-imager
•	Install full version of Raspberry Pi OS on SD card
•	Insert micro sd card into raspberry pi
•	Connect to screen, mouse, keyboard, and camera 
2.	Install the Camera 
•	To install the camera gently pull up on the CSI camera connector tab and insert the ribbon cable then gently push down on either side of the tab until the ribbon is secured. Below are instructions for the direction the ribbons face. See diagram lower on page if you need help locating CSI camera connector which is located between the Aux and micro-HDMI ports
•	Insert the cable into the Raspberry Pi camera connector with the foil end facing the micro-HDMI ports
•	The foil should be inserted facing towards the camera module when connecting the ribbon to the camera
3.	Configure OS
•	Enable SSH and 
	sudo raspi-config
•	navigate to Interfacing Options
•	navigate to SSH
•	When Prompted Select “Yes” 
•	Enable camera
•	navigate to Interfacing Options
•	navigate to camera
•	When Prompted Select “Yes”
•	Restart raspberry pi
4.	Connect to WIFI
•	Connect to the network you intend to leave your PI on.
•	Get the private IP address you can use it remotely connect to the PI from your computer later
	Hostname -I
5.	RPi Webcam Interface 
•	This will create a locally hosted website on your PI that is not connected to the internet
	sudo apt-get update
	sudo apt-get dist-upgrade
	sudo ap-get install git
	git clone https://github.com/ilyfisher/Ant_pi/blob/main/run.pyhttps://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
	cd RPi_Cam_Web_Interface
	cd bin
	mv raspimjpeg raspimjpeg-buster
	mv raspimjpeg-stretch raspimjpeg
	cd ..
	./install.sh
6.	Make dataplicity account
•	https://www.dataplicity.com/
•	Make an account
•	Copy the code from dataplicity into your Raspberry Pi terminal when prompted.
•	At the top of the page there will be a link to 'Activate Wormhole'.
•	Enable Wormhole
•	Your site should now be live and viewable from the URL dataplicity provides or the URL we copied down earlier.




[To install Temp & Hum Sensor]

1.	Connect the AM2302 Temperature & Humidity Sensor to the pin-out board on the PI
•	We will use physical pin 7 (data), pin 9 (ground), and pin 17 (3v3 power)
•	 With the AM2302 from the left + to the right – we will connect the first pin on the AM2302  to pin 17, the middle pin on the AM2302 will connect to pin to pin 7, and finally the third pin on the AM2302 we will connect to pin 9. See the diagram below to check your wiring.
  
2.	Open a terminal on the PI 
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install python3-pip
	sudo pip3 install adafruit-circuitpython-dht
	sudo apt install python3 idle3
	git clone
	cd Ant
	nano run.py
•	Now use your arrow keys to find the place that says read API Key
•	Look on your thingspeak account under the API Keys tab and paste the write API number between the spaces that follow write API
•	Now we will compile the code 
	sudo python3 run.py
	run.py & disown

3.	To graph our data online we will make a thingspeak account at https://thingspeak.com/
•	Select ‘New Channel’
•	Check two field boxes and name Field 1 Temperature & Field 2 as Humidity
•	Go to the Sharing tab and select ‘share channel view with everyone’
•	Go to the tab that says Public View
•	Select the green button that says MATLAB Visualization 
•	Select Custom (no starter code) and select Create
•	go here and paste this code where it says Enter your MATLAB code below
•	Select run and save
•	You can view your graph from thingspeak or click on the button in the picture below to generate an iframe to embed the graph in a website

                                                            

tips
Download VNC viewer on your PC and VNC server on your PI to connect with a GUI to your PI without the pi being connected to a screen and keyboard.





![image](https://user-images.githubusercontent.com/81057477/160712098-430192fc-c0ff-4926-9a0c-71f8fc728683.png)
