#  File Permissions

The 3 permissions on a Linux file are

read, r(4) - Only to read the file

write, w(2) - to write into the file

execute, x(1) - to execute the file.

These permissions are given to three types of entitities- owner of the file, group to which he belongs and others. By default the owner and group have read and write permissions; all others have read permission. These permissions can be granted/denied using appropriate commands.

## Key terminologies

  1. chmod - to change the permissions of the file.

  2. chown <username> <filename> - to change the owner of the file

  3. chown :<ugroupnmae> <filename> - to change the group ownership of the file

  4. sudo-Some commands (as above) requires certain previleges for execution.So an ordinary user can get those priveleges by usig the keyword sudo
   
  
## Exercise
### Sources


https://docs.oracle.com/cd/E19683-01/816-4883/6mb2joat0/index.html

https://docs.oracle.com/cd/E19683-01/816-4883/6mb2joat3/index.html

https://kb.iu.edu/d/abdb#:~:text=To%20change%20file%20and%20directory,%2C%20write%2C%20and%20execute%20permissions.


### Overcome challenges

Had to search on how to change the ownership and group ownership of file. Understood it by implementing chown  command.

Had to look on how to change the file permissions.Understood by implementing chmod command.

### Results

File creation(abc.txt)
##### ![LNX-05-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-01.PNG)

long list using ls -l to see the owner and group. Owner is jayashree and group is jayashree for abc.txt
##### ![LNX-05-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-02.PNG)

gave execute permission to owner
##### ![LNX-05-03img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-03.PNG)

owner has all permissions,group and others zero
##### ![LNX-05-04img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-04.PNG)

owner can read the file
##### ![LNX-05-05img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-05.PNG)

changed owner to abc
##### ![LNX-05-06img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-06.PNG)

the user(jayashree cant) read it as the owner is now abc.Also chnaged the group to abc
##### ![LNX-05-07img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-07.PNG)


the user(jayashree) cant access it


##### ![LNX-05-08img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-05/LNX-05-08.PNG)

