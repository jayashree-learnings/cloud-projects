#  Working with CLI
In Linux when compared to OS like Windows(which is more GUI focused), all the commands are done via command line interface(CLI). There are the standard inputs(keyboards) and outputs(terminal), but they can be redirected using approprite commnads as well. 

## Key terminology

  1. std inut and output
  2. redirection of outputs so that it becomes the input of another command using pipe 
  3. echo command-to print to terminal as well as to append to a file
  4. grep command - to filter lines in a file.combined with cat it can be used to filter the output from a file.
  5. Difference between > and >> operators -For output redirection, when > is used, the file gets overwritten while >> is used, it gets appended
   
  
## Exercise
### Sources

https://docs.oracle.com/cd/E19455-01/806-2902/6jc3b36dn/index.html

https://stackoverflow.com/questions/6207573/how-to-append-output-to-the-end-of-a-text-file

https://stackoverflow.com/questions/34191883/what-is-the-difference-between-and-when-using-echo-to-write-to-file



### Overcome challenges
Had to look up on how to redirect the std.ouput to a file. Understood it by implementing >> command. Searched on how to filter the output. Understood it while implementing the grep command.

### Results

lines containing techgrounds redirected to the textfile
##### ![LNX-03-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-03/LNX-03-01.PNG)

the line containing techgrounds filtered using grep and the filtered output redirected to another file
##### ![LNX-03-02img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/LNX-03/LNX-03-02.PNG)














