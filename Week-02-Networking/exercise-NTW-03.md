#  Protocols
A network protocol describes the agrement between the connected devices on how to communicate. There are a number of protocols defined by authorities like IEEE, ITU-T, IAB, ISOC, IETF,IRTF, ICANN, IANA. Each layer of the OSI stack is associated with its own set of protocols. A protocol may hve an associated port number e.g- port number 22 for SSH , port number 80 for HTTP, 23 for Telnet, 25 for SMTP.

## Key terminologies
 Port number- The number on which the application/process runs(the device listens on a port number)  

Wireshark - open source tool which helps to trce the packets in a host device.It helps to see the different protocols used during communicaton
  
## Exercise
1. Identify several other protocols and their associated OSI layer. Name at least one for each layer.
2. Figure out who determines what protocols we use and what is needed to introduce your own protocol.
3. Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.

### Sources

https://blogs.getcertifiedgetahead.com/network-osi-topics/

http://linux-training.be/networking/ch01.html#idp62993888

https://www.router-switch.com/faq/network-layers-in-osi-model-features-of-osi.html

https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet/

https://www.geeksforgeeks.org/elements-of-network-protocol/

https://www.techtarget.com/searchnetworking/definition/port-number

https://www.geeksforgeeks.org/elements-of-network-protocol/


### Overcome challenges

Had to find out what all conditions we require to call something a protocol.Understood it when read about the elements of network protocol.

### Results
1)The various protocols on different layers are

Application layer-HTTP, SSH, DNS

Presentation layer- SSL, TLS, IMAP

Session layer- various apis,sockets,NETBIOS,PPTP

transportation layer - TCP, UDP

Network layer - IP, IPsec

Data Layer - Ethernet, SLLIP, PPP,WIFI etc

Physical - Cabling protocols like Fiber, coax, Ethernet

2)The protocols are standarized and defined by orgaisations like W3c, ITU-T, IAB, ISOC,IETF,IRTF,IEEE, ICANN, IANA etc. In order to be cosidered as a protocol, it must adhere to the standard guide lines set by these organisations. It must also contain the following standard elements 

1. message encoding - A source message from the sender is encoded into signals and transmitted through a medium(wired/wireless) and the message is passed to the destination.

2. message formatting and encapsulation - The sender and receievr needs to be identified properly and there is an agreed  format  between sender and receiver

3. message size - Long messages are broken into small messages to travel across a network.

4. message timing - It checks for any delays in data passing, response time out etc.

5. message delivery option- Can be any one of the following 3 

    unicast - If there is only a single dsetination

    multi cast - One sender sends to many destinations like one to many.

    broadcast- one sender sends message to all connected receipients.

wireshark installation
##### ![NTW-03-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-03-01-InstallWireShark.PNG)

tcp protocol filtering after opening youtube on browser
##### ![NTW-03-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-TCP-02-ContainsYoutube.PNG)

udp protocol filtering when connected to zoom
##### ![NTW-03-03img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-UDP-03-ContainsZoom.PNG)















