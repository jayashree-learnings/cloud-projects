#  Asymmetric encryption
This type of encryption makes use of 2 different keys for encrpytion and decryption. The public key is is accessible by any one, but the private key is not shared. Only the  person with the private key can decrypt a message encrypted with his public key. Some of the algorithms are diffie-hellman, DSS etc. The main advantage is it's not a problem to share a public key and we dont have to keep track of many keys to share the message with many people. It is suited for small file sizes with disadvantage of being slow.

## Key terminologies
public key - key made public and accessible by anyone who wants it

private key - The key which is not shared with any one and only the receipient of the message knows it.

RSA algorithm - An algorithm which generates a public key and a private key, others being DSA, diffie-hillman,ECDSA, ECDH.

## Exercise
1. 	Generate a key pair.
2. Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. The recipient should be able to read the message, but it should remain a secret to everyone else.
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the difference between this method and symmetric encryption.

### Sources
https://www.serverbrain.org/certificate-security-2003/combining-symmetric-and-asymmetric-encryption.html#:~:text=When%20symmetric%20and%20asymmetric%20encryption%20are%20combined%2C%20the%20following%20takes%20place%3A&text=Symmetric%20encryption%20is%20used%20to,of%20the%20symmetric%20encryption%20speed.&text=Asymmetric%20encryption%20is%20used%20to%20exchange%20the%20symmetric%20key%20used%20for%20encryption

https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/public-key-encryption

https://www.geeksforgeeks.org/difference-between-symmetric-and-asymmetric-key-encryption/

https://cryptomathic.com/news-events/blog/differences-between-hash-functions-symmetric-asymmetric-algorithms#:~:text=Asymmetric-key%20algorithms%20are%20commonly,is%20called%20a%20key%20pair.

### Overcome challenges
Had to look up on how to encrypt a message using a public key and decrypt it using private key. 

### Results
The key pair was generated using an online RSA tool. The public key was shared with my colleagues and they sent me the encrypted message which I was able to decrypt using my private key. 


Public and private key generation
##### ![SEC-05-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-05/SEC-05-01-privatePublickeyGeneration.PNG)


Sharing of my public key in Slack and the encrypted messages by colleagues
##### ![SEC-05-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-05/SEC-05-02-PublicKeySharingAndEncryptedMsgs.PNG)


Decryption of message sent by collegue
##### ![SEC-05-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-05/SEC-05-03-Decryption.PNG)


Decryption of message sent by collegue
##### ![SEC-05-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-05/SEC-05-04-DecryptedMsg.PNG)













