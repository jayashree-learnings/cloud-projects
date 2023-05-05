#  Network Devices
A network consists of many devices which communicate with each other to share information. Some of the common neetwork devices are

-repeaters-regenerates the signal before the signal becomes weak. It doesnot amplify the signal

-hub -A multi port repeater. Sends dta to all connected devices

-bridge - A bridge acts like a repeater, but it can filter the packets based on mac address.

-switch - Has many ports than bridge and is used mostly in the place of bridge

-router - Work based on the ip address of the hosts. It is used to connect different networks together.

-access points- Used to create wirelss local area network (WLAN). Consists of  a transmitter and a receiver.


## Key terminologies
DHCP- Dynamic Host Configuration Protocol

DHCP lease time managemnt- IP address assigned by DHCp expires after some time.The period of validity is called DHCP lease time.   
  
## Exercise

1. Name and describe the functions of common network equipment
2. Most routers have a list of all connected devices, find this list. What other information does the router have about connected devices?
3. Where is your DHCP server on your network? What are its configurations?

### Sources

https://blog.netwrix.com/2019/01/08/network-devices-explained/

https://www.wikihow.com/See-Who-Is-Connected-to-Your-Wireless-Network

https://www.howtogeek.com/168896/10-useful-windows-commands-you-should-know/

https://www.howtogeek.com/204057/how-to-see-who%E2%80%99s-connected-to-your-wi-fi-network/

https://www.cloudflare.com/learning/network-layer/what-is-a-router/

https://www.efficientip.com/what-is-dhcp-and-why-is-it-important/

https://www.freecodecamp.org/news/what-is-my-ip-address-for-my-router-how-to-find-your-wifi-address/#:~:text=Step%201%3A%20Click%20on%20St

https://www.howtogeek.com/233952/how-to-find-your-routers-ip-address-on-any-computer-smartphone-or-tablet/

https://www.linksys.com/what-is-a-wifi-access-point.html#:~:text=An%20access%20point%20is%20a,signal%20to%20a%20designated%20area.


### Overcome challenges
First challege wa to find the ip address of the wifi-router's web interface. In the cmd of my Windows laptop, I typed ipcongig and in the result we have to look for the default gateway(Sometimes its gateway or router) of the "Wireless Lan Adapter" in the case of a wifi-router.The default gateway is the private ip address of the router. If you are connected to a wired network, we have to look for "Ethernet Adapter" . Most of the routers have a default gateay of 192.168.0.1 or 192.168.1.1. We have to check for ours.I checked and found mine.

The second challenge was to get the details of the connected devices and the configuration of the DHCP server.For that we have to type the default gateway of the wifi-router on a webrowser like chrome. It will take you to webpage of your router(In my case, the page of "ZYXEL") . Give the username and password and login. I navigated to "connectivity" window and could see the devices connected to my network.It showed the information like ip adress, mac adress, band of of internet connection,to what are they connected to. 

To see the configuration of the DHCP settings, I navigated to the "LAN" section.There I could see the details like default gateway(ip addres  of the router), subnet mask,begging ip address, ending ip address, DHCP server lease time etc.


### Results

1)A brief description of network devices have been given in the above section.

2)The information about the ip address, mac adddress etc are displayed

##### ![NTW-02-ConnectedDevices](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-02-01-ConnectedDevices.PNG)

3) The DHCP server is configured on the default gateway itself i.e. the ip address of the DHCP server and the default gateway are same.
##### ![NTW-02-DHCP-Config](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-02-02-DHCP-Config.PNG)








