#  Symmetric encryption

Encryption is the process of converting a palin human readable text into a format unreadable by humans so that only the intended party can decipher the message. In symmetric encryption, for both encryption and decryption , the same key is used. Some of the algorithms used are DES, Twofish,Serpent,AES etc.The method is considered to be suitable for large file sizes and fast. The disadvantage is that the key had to be shared and if we have to send message to many peoeple, we have to keep track of those many keys.

## Key terminologies
cryptography - the process of converting a simple text message into something which only the intended receipient can understand using different methodsalgorithmic techniques.

plain text - The original message before encryption

cipher text - the encrypted mesage which looks like a some weird combination of alphabets, numbers, characters etc so that its difficult for a third party to understand.

ceasar cipher - Ancient technique used in the dyas of Julius Ceaser. In this case if the key word is 3, then 'A' will get shifted 3 positons and become 'D', 'B' would become 'E' and so on.

## Exercise
1. Find two more historic ciphers besides the Caesar cipher.
2. Find two digital ciphers that are being used today.
3. Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. You are not allowed to use any private messages or other communication channels besides Slack. Analyse the shortcomings of this method.

### Sources
https://www.javainuse.com/aesgenerator

https://www.cryptomathic.com/news-events/blog/symmetric-key-encryption-why-where-and-how-its-used-in-banking

https://www.techslang.com/definition/what-is-symmetric-encryption/

https://www.ibm.com/docs/en/ztpf/2020?topic=concepts-symmetric-cryptography

https://delinea.com/blog/how-does-encryption-work

https://www.secplicity.org/2017/05/25/historical-cryptography-ciphers/

https://interestingengineering.com/innovation/11-cryptographic-methods-that-marked-history-from-the-caesar-cipher-to-enigma-code-and-beyond

https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/public-key-encryption

https://en.wikipedia.org/wiki/Blowfish_(cipher)

### Overcome challenges
Had to look up on how to encrypt a message an decrypt it using the key. Also had to find a way to share the key.We encrypted the key using assymetric encryption and shared the symmetrically encrypted message.

### Results
1). Some of the historic ciphers are 

1. Scytale cipher - Used by spartans.the letters were simply rearranged and the parchment was wrapped around a cylinder. The recepeint also has to use the same dimensional cylinder. It was easily decipherable by enemies.

2. enigma code - Used by german forces during world war 2.The enigma machine consisted of an old type writer looking machine with 3 rotating drums inside it and on pressing an alpahabet it generated another random alphabet

2). The 2 types of symmetric algorithms are block algorithms which includes algorithms like DES, AES,  RC5, RC6, Blowfish, IDEA and stream algorithms like RC4(DES and RC4 are considered to be insecure). In block algorithm, a fixed length of bits are encrypted in blocks of electronic data with a specific secret key. The data is held in the system-memory  as it gets encrypted.In stream algorithm, data is encrypted one digit at a time as it streams instead of being retained in the memory.

a) Advanced Encryption System, AES - Uses a 128/192/256 bit long key or a single key block cipher that encrypts or decrypts the information.  

b) Blowfish algorithm - Uses an input length of 64 bits and a variable key length of 32 to 448 bits. 

In both the cases, the same key will be shared by both the receiver and sender.

3). First using an online AES tool, an encrypted text was generated. The input given was a palin text and a 16 long character secret keyword. The encrypted message was shared via slack to the colleagues. To share the secret keyword, first it was encrypted using the public key of the colleague and then sent it to him so that he could decrypt it using his private key. Once he got the secret key, it was given as an input to the aes generator along with the encrypted message.The output was the decrypted message. In a similar manner, I could decrypt the message sent by one of my colleagues.

Encrypting the message using AES
##### ![SEC-04-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-04/SEC-04-01-AESEncryption.PNG)

Publishing the encrypted message and encrypted key(this key was encrypted using colleagues's public key) in slack
##### ![SEC-04-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-04/SEC-04-02-EncryptedMsgAndPublicKey.PNG)

The key was decrypted by his private key and the message was decrypted using RSA tool 
##### ![SEC-04-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-04/SEC-04-03-DecryptedbyVim.PNG)

Obtaining an encrypted key and message from a collegue
##### ![SEC-04-06](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-04/SEC-04-04-KeyAndMsgFromAtalla.PNG)

First his key was decrypted
##### ![SEC-04-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-04/SEC-04-05-DecryptingKey.PNG)

Finally decrypting his message
##### ![SEC-04-05](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-03/SEC-04/SEC-04-06-DecryptingMsg.PNG)















