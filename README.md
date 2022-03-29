# Ant_pi
Code to set up live cam, humidity, and temperature checker

## Writeup
[List of supplies]

- Raspberry pi 3/power supply [here](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-Listed/dp/B07BC6WH7V/ref=sr_1_6?dchild=1&amp;keywords=raspberry+pi+3&amp;qid=1618727784&amp;sr=8-6)
- Monitor, Mouse and Keyboard
- USB to Micro SD card reader [here](https://www.amazon.com/Anker-Portable-Reader-RS-MMC-Micro/dp/B006T9B6R2/ref=sr_1_3?dchild=1&amp;keywords=USB+to+Micro+SD+card+reader&amp;qid=1621221307&amp;sr=8-3)
- Raspberry pi case [here](https://www.amazon.com/Dorhea-Raspberry-Supporting-Installation-Heatsinks/dp/B07JBB9QSB/ref=sr_1_3?crid=3UVLYN5ENRPXR&amp;dchild=1&amp;keywords=raspberry+pi+3+camera+case&amp;qid=1618727670&amp;sprefix=raspberry+pi+3+camera,aps,276&amp;sr=8-3)
- Raspberry pi camera [here](https://www.amazon.com/Raspberry-Camera-Module-Megapixels-Sensor/dp/B07L82XBNM/ref=sr_1_3?dchild=1&amp;keywords=raspberry+pi+3+camera&amp;qid=1618727900&amp;sr=8-3)
- Breadboard Jumper Wires [here](https://www.amazon.com/dp/B072L1XMJR?psc=1&amp;ref=ppx_yo2_dt_b_product_details)- only get these of the ones provided with the AM2303 are too short for your project
- Heat Shrink Tubing [here](https://www.amazon.com/gp/product/B00VG9XL5U/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&amp;tag=carnivorou036-20&amp;camp=1789&amp;creative=9325&amp;linkCode=as2&amp;creativeASIN=B00VG9XL5U&amp;linkId=2f247f1dcd563eca0ebdd655d9f3245a)
- AM2302 Temperature &amp; Humidity Sensor [here](https://www.amazon.com/Gowoops-Temperature-Humidity-Measurement-Raspberry/dp/B073F472JL/ref=sr_1_2?dchild=1&amp;keywords=am2302+raspberry+pi&amp;qid=1619045823&amp;s=electronics&amp;sr=1-2)

[To make the Live video Feed]

1. First set up your raspberry pi. I used a raspberry PI 3.
  - Download raspberry pi imager using
    - _sudo apt install rpi-imager_
  - Install full version of Raspberry Pi OS on SD card
  - Insert micro sd card into raspberry pi
  - Connect to screen, mouse, keyboard, and camera
2. Install the Camera
  - To install the camera gently pull up on the CSI camera connector tab and insert the ribbon cable then gently push down on either side of the tab until the ribbon is secured. Below are instructions for the direction the ribbons face. See diagram lower on page if you need help locating CSI camera connector which is located between the Aux and micro-HDMI ports
  - Insert the cable into the Raspberry Pi camera connector with the foil end facing the micro-HDMI ports
  - The foil should be inserted facing towards the camera module when connecting the ribbon to the camera
3. Configure OS
  - Enable SSH and
    - _sudo raspi-config_
  - navigate to Interfacing Options
  - navigate to SSH
  - When Prompted Select &quot;_Yes_&quot;
  - Enable camera
  - navigate to Interfacing Options
  - navigate to camera
  - When Prompted Select &quot;_Yes_&quot;
  - Restart raspberry pi
4. Connect to WIFI
  - Connect to the network you intend to leave your PI on.
  - Get the private IP address you can use it remotely connect to the PI from your computer later
    - _Hostname -I_
5. RPi Webcam Interface
  - This will create a locally hosted website on your PI that is not connected to the internet
    - _sudo apt-get update_
    - _sudo apt-get dist-upgrade_
    - _sudo ap-get install git_
    - _git clone https://github.com/ilyfisher/Ant\_pi/blob/main/run.py_[_https://github.com/silvanmelchior/RPi\_Cam\_Web\_Interface.git_](https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git)
    - _cd RPi\_Cam\_Web\_Interface_
    - _cd bin_
    - _mv raspimjpeg raspimjpeg-buster_
    - _mv raspimjpeg-stretch raspimjpeg_
    - _cd .._
    - _./install.sh_
6. Make dataplicity account
  - [https://www.dataplicity.com/](https://www.dataplicity.com/)
  - Make an account
  - Copy the code from dataplicity into your Raspberry Pi terminal when prompted.
  - At the top of the page there will be a link to &#39;Activate Wormhole&#39;.
  - Enable Wormhole
  - Your site should now be live and viewable from the URL dataplicity provides or the URL we copied down earlier.

[To install Temp &amp; Hum Sensor]

1. Connect the AM2302 Temperature &amp; Humidity Sensor to the pin-out board on the PI
  - We will use physical pin 7 (data), pin 9 (ground), and pin 17 (3v3 power)
  - With the AM2302 from the left + to the right – we will connect the first pin on the AM2302 to pin 17, the middle pin on the AM2302 will connect to pin to pin 7, and finally the third pin on the AM2302 we will connect to pin 9. See the diagram below to check your wiring.

![Shape3](RackMultipart20220329-4-14ckt1e_html_b87a32603c0a9135.gif) ![Shape2](RackMultipart20220329-4-14ckt1e_html_47f67189a0e3e25f.gif) ![Shape1](RackMultipart20220329-4-14ckt1e_html_6034b4bbe49ab4ba.gif) ![Shape4](RackMultipart20220329-4-14ckt1e_html_d16351fa96796a58.gif) ![](RackMultipart20220329-4-14ckt1e_html_c64d78f7a3f51737.png) ![](RackMultipart20220329-4-14ckt1e_html_402ed0dd9ed839a7.png)

1. Open a terminal on the PI

  - _sudo apt-get update_
  - _sudo apt-get upgrade_
  - _sudo apt-get install python3-pip_
  - _sudo pip3 install adafruit-circuitpython-dht_
  - _sudo apt install python3 idle3_
  - _git clone_
  - _cd Ant_
  - _nano run.py_

- Now use your arrow keys to find the place that says read API Key
- Look on your thingspeak account under the API Keys tab and paste the write API number between the spaces that follow write API
- Now we will compile the code
  - sudo python3 run.py
  - run.py &amp; disown

1. To graph our data online we will make a thingspeak account at [https://thingspeak.com/](https://thingspeak.com/)
  - Select &#39;New Channel&#39;
  - Check two field boxes and name Field 1 Temperature &amp; Field 2 as Humidity
  - Go to the Sharing tab and select &#39;share channel view with everyone&#39;
  - Go to the tab that says Public View
  - Select the green button that says MATLAB Visualization
  - Select Custom (no starter code) and select Create
  - go [here](https://github.com/ilyfisher/Ant_pi/blob/main/matlab.code) and paste this code where it says Enter your MATLAB code below
  - Select run and save
  - You can view your graph from thingspeak or click on the button in the picture below to generate an iframe to embed the graph in a website

![Shape5](RackMultipart20220329-4-14ckt1e_html_6df798629e810641.gif) ![](RackMultipart20220329-4-14ckt1e_html_d3bb78b566137a12.png)

### Tips

Download VNC viewer on your PC and VNC server on your PI to connect with a GUI to your PI without the pi being connected to a screen and keyboard.
