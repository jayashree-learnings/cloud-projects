#  Identity and Access Management (IAM)

IAM is a digital security practice that consisits of a policies, programs and technologies with a view to reduce the identity related risks within a business. Identity management confirms that the person  who is trying to access something is really that person by storing the information about that person in the information database. Access management makes use of the identity management data and determines which data you have access to and what to do with it, when you have been given access to.

## Exercise
1. The difference between authentication and authorization.
2. The three factors of authentication and how MFA improves security.
3. What the principle of least privilege is and how it improves security.

### Sources

https://www.onelogin.com/learn/what-is-mfa#:~:text=Multi%2Dfactor%20Authentication%20(MFA)%20is%20an%20authentication%20method%20that,access%20management%20(IAM)%20policy.

https://www.sciencedirect.com/topics/computer-science/authentication-factor

https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661

https://www.techtarget.com/searchsecurity/definition/three-factor-authentication-3FA

https://en.wikipedia.org/wiki/Multi-factor_authentication

https://www.geeksforgeeks.org/types-of-two-factor-authentication/

https://www.geeksforgeeks.org/difference-between-authentication-and-authorization/

https://www.javatpoint.com/authentication-vs-authorization

https://www.coresecurity.com/blog/what-iam-security#:~:text=Identity%20and%20Access%20Management%20(IAM,access%20risks%20within%20a%20business.

https://www.geeksforgeeks.org/identity-and-access-management-iam-in-cyber-security-roles/

https://www.ibm.com/security/privileged-access-management?utm_content=SRCWW&p1=Search&p4=43700068018229276&p5=e&gclid=Cj0KCQjwhY-aBhCUARIsALNIC04JAmM31P5qhN7BaTj_vRtbR7az5PMWMeLQy9K2IYnf6kCdcLJs8GoaAjJNEALw_wcB&gclsrc=aw.ds

https://en.wikipedia.org/wiki/Principle_of_least_privilege

https://www.paloaltonetworks.com/cyberpedia/what-is-the-principle-of-least-privilege

https://insights.dice.com/2013/02/20/the-four-keys-to-identity-and-access-management/

https://www.checkpoint.com/cyber-hub/network-security/what-is-the-principle-of-least-privilege-polp/#:~:text=The%20Principle%20of%20Least%20Privilege%20%28POLP%29%20is%20an,and%20permissions%20required%20to%20perform%20their%20job%20role.

### Overcome challenges
Had to understand the different techniques used in security like how to find out if the claimed person is actually that person himself or not, who has access/permission to do what etc which is the difference between authentication and authorization.

### Results
1)Authentication- It is the process which ensures that a person is who he actually claims to be by verifying his identity via different techniques like 

a) password based authentication - the user is successfully authenticated only if he can provide the username and password stored in the database

b) passwordless authentication- the user gets one time password (OTP) or link on his registered phone number

c) 2FA/MFA- Requires additional information like PIN or security questions which the user can provide

d) Single Sign On- In this case, the application the user is trying to access trusts on a valid third party to verify that the claims made by the user is genuine and hence the user doesnot have to remeber different credentials for each application separarately.

Autherization - Also called authz is the process of granting a person the access to a resource and it also determines what all things the person can do with the resource. It usually works with authentication which is done first.The various techniques are

a) role based access control- User are granted access privilege depending on their profile in the organization.

b) json web token - users are verified and authorized suing public/private key pair and the relevant data is exchanged in JSON format.

c) Security Assertion Markup Language-This open standard provides authorization credential via digitally signed xml documents.

d)OAuth-is an authorization protocol which enables API to authenticate and access the requested resources.

The key differences are
1) Authentication mainly checks the identity of the user and is used to determine whether to authorize him or not to access resources. Authorization is the process of permitting the users to access resources and what to do with the resources. 

2) In authentication, both server and client are verified for their identities, while in authorization the checking is done to see if the user has access through defined roles and policies.

3) Authentication needs users login details while authentication needs users security/privilege level.

4) Authentication credentials can be chnaged by the user partially, authorization permission cannot be changed by the user.  

5) In authentication, the transmit information is done through id token and in authorization it is done through access token.

2)The three facors of authentication are
1. something the user has- includes any physical object the user has like a bank card, a security token etc
2. Something the user knows - includes something only the user knows like password, PIN etc.
3. something the user is- includes physical chatracteristic of the user like biometrics(eye iris, finger print etc.)

3)Principle of Least Privilege(PoLP) - Also known as Principal of Minimum Privilege. It implies that a user/entity should have access to data/resources to complete the required task and nothing more than that. It thus give each user only the minimum privileges which inturn helps to improve the security and prevent data breach and is considered as a best practice in authorization. Some benefits of POLP are

1.  reduction of cyber risk- As teh access is restricted, it becomes more difficult for the attacker to gain access to the system.

2.  Fewer errors - With POLP, the potential of accidental leaks, outages etc are reduced.

3.  Incresed visibilty- Implementing POLP increases the visiblity of organisation's access control systems as opposed to an all allow policy

4.  Simplified compliance - The implementation of POLP shrinks the scope of compliance responsibilities and audits thus making it easier to achieve compliance.













