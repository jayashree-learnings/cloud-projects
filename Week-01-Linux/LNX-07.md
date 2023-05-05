#  Bash Scripting

It is a convienient way of automating the repetitive tasks which otherwise requires the users to type many lines on the CLI. Bash script is a simple text file consisiting of a series of linux commands written in a certain syntax(including the if condition, for loops etc like other programming languages). The user should have the permission to execute the script and the folder containing the scripts must be added to the path variable using export command.This enables the user to execute the script from anywhere without giving the absolute path of the script.

## Key terminology

  1. $PATH -PATH variable specifies the directories to be searched to find a command.  
  
  2. #!bin/bash- tells the OS to use bash as command interpreter. This is the first line of the scrpit,starting with the shebang characters, #!.The interpreter can be Perl, python etc.

  3. variables - to store values of int, float, string etc

  4. $<var_name> -to access the value of the variable

  5.  $RANDOM - is a variable maintained by the shell. Each time it is read, it generates a value between 0 to 32767.
   
   
  
## Exercise
### Sources


https://ryanstutorials.net/bash-scripting-tutorial/bash-script.php

https://www.ibm.com/docs/hr/aix/7.1?topic=accounts-path-environment-variable

https://www.geeksforgeeks.org/shell-scripting-define-bin-bash/#:~:text=The%20shebang%2C%20%23!%2Fbin%2Fbash,time%20it%20will%20be%20bash

https://opensource.com/article/17/6/set-path-linux

https://askubuntu.com/questions/141928/what-is-the-difference-between-bin-sh-and-bin-bash

https://www.cyberciti.biz/faq/star-stop-restart-apache2-webserver/

https://phoenixnap.com/kb/bash-math

https://www.shell-tips.com/bash/math-arithmetic-calculation/#gsc.tab=0

https://blog.eduonix.com/shell-scripting/generating-random-numbers-in-linux-shell-scripting/

https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php

https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php


### Overcome challenges
Had to look on how to generate the random number within a certain range in shell script. Understood it when I started with how to print a random variable using `echo $RANDOM`  and then modified the syntax to print between 1 and 10 using `echo $[$RANDOM % 10 + 1]`.

How to implement the if-else condition in shell scripting was another challenge. Understood it when if-then-else-fi syntax was implemented.

The syntax for the arithematic operations like <= for integers in the shell scripting was also a challege. Understood it when double round brackets "(( ))" was used appropriately.

### Results

Exercise 1-To append lines
##### ![LNX-07-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-01.PNG)

Trial to see how the script is executed if path variable is not set
##### ![LNX-07-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-02-NoPATHVariable.PNG)

Executing the script after adding the absolute path of the scripts to the environmental variable
##### ![LNX-07-03img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-03-PATHAdded.PNG)

Exercise1-to install Apache2
##### ![LNX-07-04img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-04.PNG)

##### ![LNX-07-05img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-05.PNG)

Exercise 2 -random number generator

##### ![LNX-07-06img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-06.PNG)

##### ![LNX-07-07img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-07.PNG)

##### ![LNX-07-08img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-08.PNG)

Exercise 3 -random number generator with if condtion
##### ![LNX-07-09img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-09.PNG)

##### ![LNX-07-10img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-10.PNG)

##### ![LNX-07-11img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-07/LNX-07-11.PNG)





