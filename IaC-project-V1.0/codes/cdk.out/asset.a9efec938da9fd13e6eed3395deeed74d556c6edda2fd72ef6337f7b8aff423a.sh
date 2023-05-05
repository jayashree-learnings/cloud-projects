#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hi this is a web server</h1></html>' > /var/www/html/index.html










