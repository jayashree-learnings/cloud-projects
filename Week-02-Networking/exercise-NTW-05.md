# IP addresses

An IP address is a logical addresss uniquely used to identify a device connected in a network.It follows Internet Protocol, a set of rules governing the format of data to be sent via the network or local network. Depending on the versions, they are classified as private and public. Depending on whether it changes over time, they are classified as static and dynamic. According to it's internet accessibility, they are classified as public and private.A small description of each can be found in the following section:

## Key terminologies
public ip - The unique ip exposed to the internet.Provided by ISP assigned to router.

private ip - Used within for internal communication. Internet is not accessible using a private ip. 

NAT-Network Address Translation - Used to convert the private ip address (eg-in our home network)  to  public ip address. So all the devices within the network will have same public ip, thus trying to solve for the shortage of the public ip addresses.

ipVersion4 - 32 bits of 4 blocks with each block consisting of 8 bits.The value of each block ranges from 0 to 255.

ipVersion6 - 128 bits of 8 blocks with each block consisiting of 16 bits.

Static IP address - It doesnt change. Usually users enter it manually or it is assigned by the ISP.usually used by commercial VPN servers so that their employees can connect easily when working remotely and also by some websites to help visitors to access the contents easily.

Dynamic adress - It changes with time. It is assigned by DHCP server.It changes every time the host restarts the session.Usually used in home networks.
  
## Exercise
1. Find out what your public IP address is from your laptop and mobile on wifi.Are the addresses the same or not? Explain why.

2. Find out what your private IP address is from your laptop and mobile on wifi.Are the addresses the same or not? Explain why.

3. Change the private IP address of your mobile to that of your laptop. What happens then?

4. Try to change the private IP address of your mobile to an address outside your network. What happens then?

### Sources

https://support.google.com/fiber/answer/2899098#zippy=%2Cto-check-the-public-ip-address-of-your-network

https://stackoverflow.com/questions/62024695/does-your-mobile-phone-change-its-ip-address-when-you-switch-from-wifi-to-mobile

https://support.bluerim.net/hc/en-us/articles/205325706-What-is-NAT-Public-vs-Private-IPs-#:~:text=NAT%20stands%20for%20Network%20Address,is%20exposed%20to%20the%20Internet.

https://whatismyipaddress.com/private-ip

https://phoenixnap.com/kb/public-vs-private-ip-address

https://kb.zyxel.com/KB/searchArticle!gwsViewDetail.action?articleOid=013981&lang=EN

https://support.google.com/fiber/answer/3547208?hl=en#:~:text=What%20is%20the%20difference%20between,connect%20and%20change%20over%20time.

https://whatismyipaddress.com/dynamic-static

https://www.geeksforgeeks.org/difference-between-static-and-dynamic-ip-address/

https://www.security.org/vpn/static-vs-dynamic-ip-address/

### Overcome challenges
The first challenge was how to find the public ip of my laptop and mobile. Understood that we can go to the link 
https://www.whatismyip.com/ and it displays the public ip of the device. So I navigated to that link in both mobile phone and laptop and found the public ip of both .Th public ip of both the devices were same.

The second challenge was to find out the private ip of my laptop. In the cmd prompt, I ran the command ipconfig and found that both ipv4 of my laptop under the "Wireless LAN adapter Wi-Fi" . Since its a private ip it starts with 192.

The third challenge was to find the private ip address of my mobile phone. For that I opened the web browser interface of my router in google chrome browser by typing the default gateway ip address. Giving the router credentials,I could navigate to the connected devices section, which showed both my laptop and mobile phone being connected to my wifi-router. From there, I could get the private ip of the mobile. The private ip address of each of the connected devices were different.

Another challenge was how to interchange the private ip address of mobile and laptop. Was able to do so by changing the static dhcp configurations.The mac address and ip address need to be specified. So by selecting the mac address of the mobile, the ip address of the laptop was given.Similarly, I selected the mac address of the laptop and gave the ip address of the laptop. After applying these settings, reboot the router. Login again and on navigating to the window of connected devices, it can be seen that the ip addresses of both the devices have been interchanged.

Another challenge was to identify an address outside my home network range. For that I looked into the starting and end ip addresses configured in the DHCP server and understood that addresses from 192.168.1.2 to 192.168.1.254 can be assigned to the hosts connected to the router of my home network. So I tried to assign 192.168.2.0 which is outside the existing ip adress range and found that it throws error.

### Results
The private ip addresses of all the devices connected to the router are unique.

The public ip address of all the connected devices to the router are same.The router makes use of NAT process to assign a single public ip address to all the devices and after sending or receiving data through the public ip address, router passes that data to the specific device using the unique private ip address.

Since public ips are assigned by ISP, users cant change it. Private ip of connected devices to a router can be changed  via router's admin dashboard(private ip of a laptop can be changed via cmd prompt using ipconfig /release followed by ipconfig /renew).

When tried to assign an ip address to the laptop ouside of the home network, it throws error.  

public ip of my devices
##### ![NTW-05-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-05-01-publicip.png)

private ip of laptop
##### ![NTW-05-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-05-02-privateip-Laptop.PNG)

connected devices and their ip and mac addresses
##### ![NTW-05-03img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-05-03-privateips-routerinterface.PNG)

changing the ip of laptop to that of mobile
##### ![NTW-05-04img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-05-04-ChangedLatop-ip.PNG)

changing the ip of mobile to that of laptop
##### ![NTW-05-05img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-05-05-ChangedMobile-ip.PNG)

interchanged ips
##### ![NTW-05-06img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-05-06-InterChangedIPs.PNG)

when assigning a new ip outside the existig dhcp range it throws error(current dhcp range is in the series of 192.1 and when tried to give 192.2, iit threw error)
##### ![NTW-05-07img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-05-07-InvalidIPAddr.PNG)
