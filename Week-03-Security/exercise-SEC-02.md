#  Firewalls

Firewalls mainly a part of network security controls the traffic by allowing or denying it.It examines each data packet and decide if the packet is a source of threat and discards the packets accordingly.

## Key terminologies

Stateful firewall - Can moitor and detect staes of all traffic based on traffic patterns and flows even those not manually given by the administrator. It maintains a state table.Maintains context about active sessions and use state information to speed packet processing.Security is high, but low speed.Based on dynamic packet filtering

Stateless firewall - Can focus only on individual data packet and check its source, destination port number ,ip address and other parameters set by the administrator beforehand. It just filters based on the information in packet headers(header info, ip address, port number). It has ACL rules and doesnot relate to connection state. Security is less, but speed is fast. Based on static packet filtering.

Hardware firewall - Physical devices each with its own computing resources. More suitable for organisations with large networks.Installed between the computer and internet so that it will not be accesible. Can block a a domain or website.

Software firewall -Installed on individual devices. Are more expensive because of the resources utilization,but gives more control. Blocking can be done on key words.

ufw - uncomplicated firewall. It i the default firewall configuration for ubuntu.If enabled, by default it denies the incoming traffic and allows the outgoing traffic.

## Exercise
1. Install a web server on your VM.View the default page installed with the web server.

2. Set the firewall to block web traffic, but allow ssh traffic. Make sure the firewall is working.

### Sources

https://linuxize.com/post/how-to-setup-a-firewall-with-ufw-on-ubuntu-20-04/#:~:text=Ubuntu%20ships%20with%20a%20firewall,as%20the%20name%20says%2C%20uncomplicated.

https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04

https://www.cdw.com/content/cdw/en/articles/security/stateful-versus-stateless-firewalls.html#:~:text=Stateful%20firewalls%20are%20capable%20of,preset%20rules%20to%20filter%20traffic.

https://www.fortinet.com/resources/cyberglossary/stateful-vs-stateless-firewall

https://ipwithease.com/stateless-vs-stateful-firewall/

https://www.itsasap.com/blog/stateful-vs-stateless-firewall-differences

https://www.geeksforgeeks.org/stateless-vs-stateful-packet-filtering-firewalls/

https://biztechmagazine.com/article/2020/11/stateful-vs-stateless-firewalls-whats-difference-perfcon

https://www.geeksforgeeks.org/difference-between-hardware-firewall-and-software-firewall/


### Overcome challenges
Had to find out how the firewalls work on ubuntu server. Understood it while implementing the ufw commands. The default page of apache2 was accessible initially. After denying the traffic by setting the deny rule, the page became inaccessible.

### Results
Apache2 was installed already while doing an exercise on linux. It is working as can be seen below.
##### ![SEC-02-01-Installnmapimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-02-01-ITWorks.PNG)

First ssh is enabled and only then ufw is enabled , else by default ufw blocks all incoming traffic.(allows all outgoing)
##### ![SEC-02-02-ufwEnablenmapimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-02-02-ufwEnable.PNG)

The service apache is denied 
##### ![SEC-02-03-denyApachepimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-02-03-denyApache.PNG)

The site is unreachable now
##### ![SEC-02-04-unreachableWebsiteimg](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/SEC/SEC-02-04-unreachableWebsite.PNG)












