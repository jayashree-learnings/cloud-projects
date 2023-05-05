#  Cron jobs

A cron job is a linux command used to schedule tasks to be executed some time in the future.Cron is a daemon - a background process executing non interactive jobs. The scripts to be executed on a scheduled time basis can be added to the cron tab. The time is specified by five * marks, each representing minutes,hours,dom(day of the month),mon(month),dow(day of the week).The range for the these values is as follows

minutes - 0 to 59

hours - 0 to 23

day of the month - 1 to 31

month - 1 to 12

day of the week - 0 to 6 (sunday = 0)


## Key terminologies

  1. crontab -l - to display the contents of the crontab file of teh currently logged user.
  2. crontab -e - to edit the current users cron jobs.
  3. date - a command that displays the current date and time.
  4. df - to check the the disk space. using the optional --output, the result can be filtered. 
  
## Exercise
### Sources

https://manpages.ubuntu.com/manpages/kinetic/en/man1/date.1posix.html

https://www.hivelocity.net/kb/what-is-cron-job/

https://crontab.guru/every-week

https://itsfoss.com/check-free-disk-space-linux/

https://askubuntu.com/questions/634173/how-to-get-date-and-time-using-command-line-interface

### Overcome challenges

Exercise 1

Had to look for the command to print the the current date and time. Understood it while implementing the date command to print the current date and time on terminal.

Exercise 2

Searched on how to check the disk space. Understood it while using the df command.
 
The diskSpace_logs.txt inside /var/log can be created with root user privileges only. So created the file with sudo command. Only the owner root can write into the file(he has read permission also).When tried to modify the file as a normal user, it throws error.

Created a scripting file in cat /home/jayashree/scripts/. Changed the ownership to root user and gave execute permission to the scripts.Else it throws error.

When tried to add the script to the account of normal user('jayashree'), it failed.So added it to the crontab of the root user account to print the diskSpace-logs at one minute.Validated the result by printing the output of the diskSpace_logs.txt at one minute.

After the validation that the script is working fine for one minute, modified the chronetab to perform the job for one week. 

### Results
Exercise 1
##### ![LNX-08-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-01.PNG)

ExecutingScript
##### ![LNX-08-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-02.PNG)

Registering into cron table
##### ![LNX-08-03img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-03.PNG)

Exercise 2
Error when tried to create a file as a normal user in `/var/log` 
##### ![LNX-08-04img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-04.PNG)

created log file as rotuser
##### ![LNX-08-05img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-05.PNG)

Script to write diskspace logs
##### ![LNX-08-06img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-06.PNG)

Error when trying to execute as jayashree
##### ![LNX-08-07img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-07-ErrorWhenExecutingAsNormalUser.PNG)

Changed the owner of the script
##### ![LNX-08-08img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-08-ChangedPermissionAndOwnership.PNG)

Error when tried to add crontab to the normal user jayashree
##### ![LNX-08-09img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-09-LogsWritableByRootOnly.PNG)


Added to the Crontab of root
##### ![LNX-08-10img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-10-AddedToCrontabOfRoot.PNG)

validation to see if it works for one min
##### ![LNX-08-11img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-11-ValidationForOneMin.PNG)

Weekly Crontab
##### ![LNX-08-12img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-08/LNX-08-12-FinalCronTabForWeekly.PNG)











