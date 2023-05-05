#  Passwords
Passwords are a part of the "something you know" category. Unprotected passwords thus threatens the security. Hashing converts the plain text paswword to unintelligible numbers and letters. 

## Key terminologies

Salting - Adding random characters to a password before hashing it so that even same passwords generates different hashed values.  

SHA - Secure Hash Algorithm.A hashing algorithm others being bycrypt etc. 

Rainbow table - A precomputed table to reverse hash functions. Mainly used to crack password hashes.

MD5 - Message Digest method 5 - Algorithm to digest 128 bit from a string of any length.

## Exercise
1. Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
2. Find out how a Rainbow Table can be used to crack hashed passwords.Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.
03F6D7D1D9AAE7160C05F71CE485AD31
03D086C9B98F90D628F2D1BD84CFA6CA
3. Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table. Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.

### Sources
https://www.pingidentity.com/en/resources/blog/post/encryption-vs-hashing-vs-salting.html#:~:text=Hashing%20is%20a%20one%2Dway%20process%20that%20converts%20a%20password,to%20obfuscate%20the%20actual%20password.

https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/

https://www.theguardian.com/technology/2016/dec/15/passwords-hacking-hashing-salting-sha-2

https://www.authgear.com/post/password-hashing-salting

https://www.okta.com/blog/2019/03/what-are-salted-passwords-and-password-hashing/

https://crackstation.net/hashing-security.htm

https://sectigostore.com/blog/why-using-a-password-salt-and-hash-makes-for-better-security/

https://www.cyberciti.biz/faq/understanding-etcshadow-file/

https://stackoverflow.com/questions/18035093/given-a-linux-username-and-a-password-how-can-i-test-if-it-is-a-valid-account

https://www.mvps.net/docs/the-gentent-command-individual-view-of-information-in-linux/

### Overcome challenges
Had to look up the difference between hashing and symmetric encryption wrt password storing. Had to see how to crack the passwords using rainbow table. Another challenge was despite being giving the same password for the user, why the hashed passwords were different. Understood it when I read about salting which adds a different string and hence produces a different hash for the same password.

### Results
1) Hashing maps data of any size to a fixed length using an algorithm. The main difference between hashing and encryption is that hashing being a one way function, it is not feasible to reverse-hash the data. Encryption being a 2-way function it is possible to decrypt the cipher text. Encryption tries to protect the data in tact while hashing verifies that data is not altered.

2) The first password was cracked using rainbow table. The second password being a random strings couldnot be cracked. 

3) A new user was created with the password 12345. Compared the hashed password with a colleague. As expected both were different. Also the hashed password couldnot be cracked using the rainbow table. In linux, when we use getent shadow command to see the password of the user, the hash field consists of 3 parameters. $6$ means the sha-256 algorithm was used, then the hashed password which consists of the salt portion and the password portion. This password portion was used as an input to the rainbow table and it could not be cracked.

Cracking the first password in rainbowtable
##### ![SEC-07-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-07/SEC-07-01-CrackPassword.PNG)

Unable to crack the second password
##### ![SEC-07-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-07/SEC-07-02-UnbleToCrackpwd.PNG)

Creating a new user and password for the user
##### ![SEC-07-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-07/SEC-07-03-UserAddAndpwd.PNG)

Display the password of the user
##### ![SEC-07-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-07/SEC-07-04-PasswdOfuser.PNG)

Unable to crack the password of the user
##### ![SEC-07-05](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-07/SEC-07-05-UnableToCrackPasswd.PNG)

Comparing the password with a colleague;both are different
##### ![SEC-07-06](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-07/SEC-07-ComparisonOfPasswdWithWim.PNG)
















