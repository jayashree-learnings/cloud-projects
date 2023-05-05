#  Users and Groups

Linux supports multiple users simultaneously. Each user has their own account. The root user has all the permissions to execute any  command whereas other users have only restricted previleges. The priveleges of a user can be changed by adding them to the sudoers list. Similarly when a user is created,he belongs to a group with the same name. A user can be added or deleted to/from a group. 

## Key terminology

  1. useradd- to create a new user
  2. groupadd- to create a group
  3. passwd - to set the password for the user
  4. usermod -aG - add user to a group.
  5. /etc/group - file in which all groups are stored
  6. /etc/passwd-file in which all users are stores
  7. /etc/shadow- file which stores encryoted passwords.
  8. visudo- file to which users can be added to change their permisssions.
  9. getent group grouop-name-to see the details of that groupname
   
  
## Exercise
### Sources

https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file

https://manpages.ubuntu.com/manpages/bionic/en/man5/passwd.5.html

https://www.cyberciti.biz/faq/howto-linux-add-user-to-group/

https://medium.com/analytics-vidhya/how-to-add-users-to-sudoers-file-in-ubuntu-e89c24b7369d


### Overcome challenges
Had to look up how to add a user to a sudoer list so as change the privileges.Understood by using the visudo command which opens the /etc/sudoers file using vi editor. I was able to add a new user to the file and grant the user the same previleges as the root user and enabled passwordless authentication to execute the commands. 

### Results

adding the uer,setting the user's passwd,creating group and finally trying to display /etc/passwd content, but list is long
##### ![LNX-04-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-01.PNG)

using grep to get the deatils of the user js, tring to list contents of /etc/groups, but again its a long list
##### ![LNX-04-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-02.PNG)

using grep to get the details of admingroup, adding the user js to admingroup
##### ![LNX-04-03img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-03.PNG)

displaying the content of /etc/sahadow with grep to see the passwd of the user js
##### ![LNX-04-04img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-04.PNG)

adding user js in the visudo file and enabling passwordless privilege so that when the user performs sudo commands it wint propmt for passwd
##### ![LNX-04-05img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-05.PNG)
logged in as the user js
##### ![LNX-04-06img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-06.PNG)

user js able to do sudo commands without getting prompted for passwd
##### ![LNX-04-07img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-07.PNG)

checking the credentials of users js and abcd using id command
##### ![LNX-04-08img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-08.PNG)

using getent group groupname to see the users in that group
##### ![LNX-04-09img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-04/LNX-04-09.PNG)

