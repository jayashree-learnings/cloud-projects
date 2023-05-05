#  Network Detection

With the current internet boom, its extremely important to monitor the activities going on in the network and analyze them thoroughly. This helps to reduce the threats the network is exposed to. There are many tools availble of which the most commonly used ones are Nmap and wire shark.

## Key terminologies

Nmap - Network Mapper is a free and open source tool used for vulnerability checking, port scanning and network mapping.This program scans the network and enlists the ports, devices etc which helps the users understand the details of the connection status.

Wireshark - Free and open source which helps to capture network packets and drill down into it, thus helping with network analysis and security.

## Exercise
1.scan the network of your Linux machine using nmap. What do you find?

2.Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser. (Tip: you will find that Zoom is constantly sending packets over the network. You can either turn off Zoom for a minute, or look for the packets sent by the browser between the packets sent by Zoom.)

### Sources

https://unixcop.com/how-to-install-and-use-nmap-on-ubuntu/

https://linuxways.net/ubuntu/how-to-install-nmap-on-ubuntu-20-04/

https://www.youtube.com/watch?v=4t4kBkMsDbQ

https://www.holmsecurity.com/resources/what-is-nmap#:~:text=Internet%20security%20companies%20can%20use,open%20ports%20and%20other%20weaknesses.

https://www.networkworld.com/article/3296740/what-is-nmap-why-you-need-this-network-mapper.html

https://www.redhat.com/sysadmin/use-cases-nmap

https://en.wikipedia.org/wiki/Wireshark

https://nmap.org/book/man.html



### Overcome challenges
Had to find out how to install nmap. Had to find the command to scan the system. Understood it on implementing the 'nmap host-address'. 

The challenge with wireshark was how to find the required packets. Understood it when I could filter packets based on filtering protocols like udp contains zoom. We can filter out the packets based on protocols.

### Results
1.On scanning with nmap, it shows which processes are running on which ports with their port number and state.Also when used with ip address/24,
it showed the details of other instances as well.  
nmap installation
##### ![SEC-01-01-Installnmapimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-01-Installnmap.PNG)
net-tools installation(needed to use the command ifconfig)
##### ![SEC-01-02-net-toolsimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-02-net-tools.PNG)
ifconfig command
##### ![SEC-01-03-ifconfig](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-03-ifconfig.PNG)
namp on my server
##### ![SEC-01-04-namp-scanimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-04-namp-scan.PNG)
nmap on other instances
##### ![SEC-01-05-nmapOtherInstancesimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-05-nmapOtherInstances.PNG)

2.On turning off zoom, the packets sent and received from zoom were stopped.The only packets visible were the packets sent and received by the web browser.The website of cisco was open and on filtering it using udp contains cisco, I could see the data exchange between the browser and the website.I could see that DNS protocol was used to resolve tthe website name to its ip address.  
Before zoom connection, if you filter, wont be dispalyed because packets have not started to send and receive
##### ![SEC-01-06-beforeZoomConnectionimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-06-beforeZoomConnection.PNG)
The number of packets increases after connecting to zoom
##### ![SEC-01-07-AfterZoomConnectionimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-07-AfterZoomConnection.PNG)
the number of packets decreases after disconnection. The packet number 21887 was the last packet corresponding to zoom and on disconnection, the communication has stopped. 
##### ![SEC-01-08-zoomAfterDisconnectionimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-08-zoomAfterDisconnection.PNG)
on visiting the wbsite of cisco,the relevant information can be analysed.The source mac address is the mac address of my laptop and destination mac address is the mac address of roueter. The source ip is the ip address of my laptop and destination ip is the ip address of my router which has in built DNS server.Also the source port is the port number of my local machine, while destination port is 53 which corresponds to DNS server.
##### ![SEC-01-09-VisitWebsiteimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-01-09-VisitWebsite.PNG)















