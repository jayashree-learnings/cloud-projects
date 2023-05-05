#  Public Key Infrastructure(PKI)
PKI combines encryption and authentication which makes online communication trustworthy.The public keys are a part of encryption and they help to authenticate the identity of the communicating parties.the 3 entities which form PKI maintaining confidentiality, Integrity and Authority (CIA) are server, client and CA(certification authority).

## Key terminologies

Digital certificate -Electronic credentials issued by a trusted third party authority. It verifies the identity of the owner and also that the owner owns the public key. Contains information like certificate owner's name, owner's public key and expiration date, certificate isssuer's name, certificate issuer's digital signature. PKI solves the man in the middle problem. The public key of any user can be replaced by a hacker;so there is no way to determine whose public key it actually is. When it is sent with a digital certificate it is ensures that the public key actually belongs to that user.

x509 - Digital certificates are called as x.509 certificates because they are based on x.509 ITU standard

SSL- Secure Sockets Layer. Standard technology to keep internet connection secure and to safeguard sensitive data sent between 2 sysytems like a website and a web browser, 2 servers etc.

TLS - Transport Layer Security.More secure than SSL.

CA - Certificate Authority which issues, revokes and validates identities and  certifictes(For web baed connections, the common CAs are DigiCert, GoDaddy, GlobalSign, IdenTrust,Sectigo etc)

## Exercise
1. Create a self-signed certificate on your VM.
2. Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
3. Find the list of trusted certificate roots on your system (bonus points if you also find it in your VM).
	
### Sources
https://www.linode.com/docs/guides/create-a-self-signed-tls-certificate/

https://www.howtouselinux.com/post/certificate-chain

https://geekrewind.com/how-to-create-self-signed-certificates-on-ubuntu-linux/#:~:text=To%20create%20a%20new%20Self,for%20the%20example.com%20domain.&text=The%20command%20details%20are%20as,and%202048%20bit%20RSA%20key.

https://www.arubacloud.com/tutorial/how-to-create-a-self-signed-ssl-certificate-on-ubuntu-18-04.aspx

https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04

https://www.howtouselinux.com/post/install-a-ca-certificate-on-linux

https://en.wikipedia.org/wiki/Public_key_infrastructure

https://www.keyfactor.com/resources/what-is-pki/

https://www.venafi.com/education-center/pki/how-does-pki-work

https://www.tutorialspoint.com/cryptography/public_key_infrastructure.htm

https://www.geeksforgeeks.org/public-key-infrastructure/

https://www.csoonline.com/article/3400836/what-is-pki-and-how-it-secures-just-about-everything-online.html

https://www.websecurity.digicert.com/security-topics/what-is-ssl-tls-https

https://www.ssl.com/faqs/what-is-an-x-509-certificate/


### Overcome challenges
Had to understand the issues solved by PKI. Had to look up on how to create self signed certificate in VM. Understood it with the implementation of openssl tool. The following parameters were specified.

req -x509 - modifies the req(request to genearte CSR) to get a self signed certificate instead of the usual CSR

-newkey rsa:4096 - to create a new key of size 4096 bits long. 

-keyout - tells openssl where to place the private key

-out - this tells openssl where to place the certificate created. 

-sha256 - geenrate the certificate request using 256 bit SHA(Secure Hash Algorithm)

-days - The validity of certificate

-nodes - create a certificate without passphrase.else passphrase will have to be entered each time the application using the certificate gets restarted. 
Finally the permission of the generated key was changed so that only the root has read permission on it.

The second challenge was to find the certification paths of some common websites. Could understand it on clicking the lock icon of the web browser url and navigating to certificates. 

Another challenge was to find the certification path in the local machine.I navigated to the settings- privacy and security-security and chose the manage certificate option.The various root CAs were dispalyed. On the VM, we can display the certificates by listing the contents of the /etc/ssl/certs

### Results
1) A self signed certificate was created using the openssl tool. 

Certificate generation
##### ![SEC-06-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-01-CertificateGenerate.PNG)

Displaying contents of the certificate
##### ![SEC-06-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-02a-DisplayContentsCertificate.PNG)

##### ![SEC-06-02b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-02b.PNG)

Changing the permission of key
##### ![SEC-06-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-03-KeyPermissionChange.PNG)

2)certification path of google
##### ![SEC-06-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-04-CertificationPathGoogle.PNG)

##### ![SEC-06-05](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-05-CertificateGoogleDetails.PNG)

Certification path of techgrounds
##### ![SEC-06-06](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-06-CertificateTG.PNG)

##### ![SEC-06-07](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-07-TGCertificateDetails.PNG)

Certification path of ING
##### ![SEC-06-08](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-08-INGCertificate.PNG)

##### ![SEC-06-09](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-09-INGCertificateDetails.PNG)

Certificate details in local system
##### ![SEC-06-10](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-10-RootCertificateInLocalSytem.PNG)

certificate details in V.M.
##### ![SEC-06-11](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-06/SEC-06-11-Certs-VM.PNG)
















