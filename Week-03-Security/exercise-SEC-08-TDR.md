#  Detection Response and Analysis

Threat detection, response and analysis refers to the set of tools which helps to identify the threats immediately, take fast action and finally to analyse how it happened.It helps to stop known threats, unknown emerging threats based on behavioural models and highly evasive massive threats capable of evading traditional malware defenses.

## Key terminologies
1) Recovery Point Objective, RPO - The maximum data the company can afford to loss in the case of a disaster

2) Recovery Time Objective RTO - The maximum time the company/business can afford to be on the downside/offline.

3) Intrusion Detection System IDS -It is a software that monitors a system or a network for intrusions or malicious activities. The main purpose is to identify the threat before it infilters the system and it wont take any direct acction against the threat. Suitable when you dont want to slow down the traffic even in the presence of an issue. The detection method can be signature based (based on known malicious sequence) or anomaly based (based on machine learning, a trusted model is set up and anything that doesnt match it is reported as threat). The IDS can be classiied as Network IDs(monitors an entire subnet and tries to match the traffic with known pattern), Host IDS (monitors the particular host only), protocol IDS(Positioned at the front end of a server, monitoring the protocol between the user and server), Application Protocol IDS(positioned on a group of servers to monitor application specific protocols) and hybrid IDS (a combination of 2 or more of the above mentioned different types).

4) Intrusion Prevention System IPS -Also called intrusion detection and prevention system and is like an extension of IDS. it can send alarms, drop malicious packets, reset the connections. Suitable if attacks need to be blocked on the detection even if it is done by closing all the traffic. the differnt types are network IPS(monitors entire entire network for suspicious protocol activies), Wireless IPS(looks for suspicious wireless traffic), Network behaviour analysis (looks for distributed denial of service attacks, malwares), Host based IPS(positioned on a single host and scans the events on that host only).

5) Incident response plan strategy - The various phases of incident response plan are 
 1. Preparation - In this phase, security issues are prioritized, most sensitive assets are identified, the critical security incidents the team should focus on is decided.

 2. Identification - In this phase, the most important questions of who, what, where, why and how are addressed.

 3. Containment- The goal is to prevent the further spread of the incident and it can be short term (eg-isolating  network segments, taking down infected production servers etc) or long term(applying temporary fixes to the affected sysytems, while buiding new clean ones)

 4. Eradication- Immediate removal of the malware and threats is the focus of this phase

 5. Recovery- The focus here is on to decide from which time and date to restore operations, how to verify that the affected systems are back to normal and monitoring to ensure activity is back to normal

 6. lessons learned- It is performed during the two weeks of the incident-occcurance so that it is still fresh in team's mind. The objective is to complete the documentation of the incident, investigate its scope and understand where response team was effective, identify the areas which need improvement.

6) Systems hardening - As per the NIST defintion "it is a process intended to eliminate a means of attack by patching vulnerabilities and turning off essential services.". It is a collection of tools, techniques and best practices to reduce vvulnerability in technology applications, systems, infrastructure, firmware etc. It includes

- Server hardening - It includes securing the ports, data, componenets at hardware, software and firmware layers. Some of the common practices include using strong password policies for users, implementing MFA, using encryption method to protect sensitive data etc.

- Software application hardening - It involves implementing additional security to protect the applications deployed on the server. The common practices include using firewalls, installing IPS, Ids, software-based data encryption, using anti virus, malware etc. 

- Operating system hardening - The focus is to secure the base Operating System which gives permission to the installed application to do certain things on the server. Some common practices are limiting the logging in of users, encrypting the HDD/SSD that stores and hosts your OS, removing unnecessary drivers etc. 

- Database hardening - Aim is to secure data store of an enterprise achieved by a 3-step process of 1) limiting user privileges/access 2)disabling unwanted database services 3)encrypting the data stored. Some of the common techniques include updating/patching DBMS, enforcing strong passwords, removing unwanted services and functions etc. 

- Network hardening - Involves strengthening the communication channel between two ports mainly done using IPS and IDS along with firewalls. The common techniques include auditing network rules, network access privileges, encrypting traffic, disabling network devices being not in use.


7) Disaster recovery options - The various disaster recoveryoptions are

1. Data back up - it is the basic recovery option which is relevant due to the rise of ransomware.Following a 3-2-1 policy(take 3 copies of data, keep 2 copies on different back up mediums, keep 1 copy offite), this option also ensures that back ups are working fine, data restoration is tested, the devices are backed up etc.

2. Virtual disaster recovery plan- It is an improvised version of data back up plan.In this case, the entire IT infrastructure is backed up on cloud server. It includes the replication of entire IT infrastructure, vitual machines to run the infrastucture etc. It is less reliant on hardware services and virtual environment can be restored to devices at any location.  

3. Disaster recovery as a service, DRAAS- In this case, a complete copy of the infrastructure is kept in a third party cloud environment and all verifications of back ups and security are handled by them so that business owner doesnt have to purchase and maintain anything separately.

4. Hot site disaster recovery - This option is most suited for organisations like medical facilities, financial institutions cannot afford to being down even for a few hours. In this case, the secondary site is always up and running with the data and devices connected to necessary sysytems and infrastructure in place.   

5. cold site disaster recovery - Less expensive when compared with hot site disaster recovery plan. It involves renting space to store the servers and related facilities when needed, but it wont be up and running 


## Exercise
1. A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
2. An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?


### Sources
https://www.geeksforgeeks.org/aws-disaster-recovery-strategies/

https://www.geeksforgeeks.org/intrusion-prevention-system-ips/

https://www.geeksforgeeks.org/intrusion-detection-system-ids/

https://geekflare.com/ids-vs-ips-network-security-solutions/

https://www.beyondtrust.com/resources/glossary/systems-hardening

https://www.trentonsystems.com/blog/system-hardening-overview

https://www.geeksforgeeks.org/what-is-system-hardening/#:~:text=The%20idea%20of%20system%20hardening,part%20of%20system%20security%20practices.

https://www.techtarget.com/searchdisasterrecovery/definition/disaster-recovery

https://cloudian.com/guides/disaster-recovery/disaster-recovery-solutions-top-5-types-and-how-to-choose/

https://www.acronis.com/en-us/blog/posts/threat-detection-response/

https://www.exabeam.com/incident-response/incident-response-plan/

### Overcome challenges
Had to understand the difference between IPS and IDS. 


### Results

1) As per the defintion RPO is the maximum data the organization can afford to lose. Since the back up is done daily (interval of 24 hrs), the maximum data that can be lost is the last 24 hours of data which is the RPO. The actual amount of data lost is the data lost between the time the disaster happened and the previous back up. 

2) AS RTO is the amximum time needed for the system to get up and running, it is 8 minutes as given in the question.













