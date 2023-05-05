#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo "<html><h1> Fear kills more dreams than failure ever will ! says web server $(hostname -i)  </h1></html>"  > /var/www/html/index.html










