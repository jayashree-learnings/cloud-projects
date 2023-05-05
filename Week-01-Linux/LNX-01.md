#  Connecting to remote server

  Connection to a remote server can be either password based authentication or key-based authentication.In password based authentication, the user logins in by giving his username and password.In the key based authentication, public key and private key is made use of. The public key is copied to the server to which we want to SSH into.   
  For this exercise, the given pem file was used to connect to the remote ubuntu server.The connection can be done using tools like putty/mobaXterm or we can use Windows powershell. Both the methods to access the server have been made use of .    
 
## Key terminology

 1. ssh-A networking protocol used to access remote servers securely.
 2. port number -in a network of connected devices, port number helps to identify the unique processes or applications running on it
3. username- the acccount used to login to the system
4. ip address - logical address of a host in a network

 
## Exercise
### Sources

https://www.simplified.guide/ssh/connect-to-different-port

https://stackoverflow.com/questions/34045375/connect-over-ssh-using-a-pem-file

https://superuser.com/questions/1666505/how-to-set-600-permission-on-a-pem-file-in-w10


### Overcome challenges
The connection to the remote server was made using mobaXterm(a tool similar to putty for remote-connections) for the first time . Had to give the path to the pem and change the default port number from 22 to 58007.

For the second time, remote-server access was done via windows power shell. 
Had to search how to specify the pem file location and how to specify a different port number in CLI.(If done via windows power shell for the first time, the permission of the key needs to be set to 600. else it throws bad permissions error.)
The command given was

ssh -i pemfile-location username@ipaddress -p portnumber 
where 

i is the identity file(file from which the identity key or the private key is read for public key authentication)

-p - port to connect to remote server

username - account used to login to the server

ip address - ip address of the remote server.

### Results

connecting using mobaxterm
##### ![LNX-01-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-01/LNX-01-01.PNG)

connecting using windows powershell
##### ![LNX-01-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-01/LNX-01-02.PNG)
checking the version of linux for validation
##### ![LNX-01-03img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-01/LNX-01-03.PNG)











