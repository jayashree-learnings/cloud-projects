# Requirements of v1.1

In addition to the following requirements of version 1.0 ,


    ●	All VM disks must be encrypted.

    ●	The web server must be backed up daily. The backups must be retained for 7 days.

    ●	The web server should be installed in an automated manner.

    ●	The admin/management server must be reachable with a public IP.

    ●	The admin/management server should only be accessible from trusted locations (office/admin's home)

    ●	The following IP ranges are used: 10.10.10.0/24 & 10.20.20.0/24

    ●	All subnets should be protected by a subnet-level firewall.

    ●	SSH connections to the web server should only be established from the admin server.

the below stated requirements were also added in the new version

    ●	The web server should no longer be accessible directly on the internet. Ideally, the client would like to see a proxy intervene. Also, the server will no longer have to have a public IP address.

    ●	Should a user connect to the load balancer via HTTP, this connection should be automatically upgraded to HTTPS.

    ●	In doing so, the connection must be secured with at least TLS 1.2 or higher.

    ●	The web server should undergo a 'health check' with some regularity.

    ●	Should the web server fail this health check, the server should be automatically restored.

    ●	Should the web server come under sustained load, a temporary additional server would have to be started up. The customer believes that no more than 3 servers total would ever be needed given past user numbers.













