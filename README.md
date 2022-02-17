# cleanser

Do you also like swearing in comments but hate the idea of getting expelled from your uni for leaving in a bad word in one of your assignments by accident (hey, it's really hard to control what you say on those late nights). Fear not, just run your code through this python script and rest assured any profanities, no matter how gut wrenching or terrible, will be picked up and brought to your attention.

# Installation
1. clone the repo
2. add the python script to an alias in your `.bashrc` or some equivalent (i'm too lazy to make install script or anything fancy)

# Use
See [this wiki page](https://github.com/peipacut/cleanser/wiki/writing-a-.cleanse-file) on writing a cleanse file **which is a very important step for using this application**. tldr; 
1. make a file called `.cleanse` in your project directory,
2. add it to the `.gitignore` (if it exists) and 
3. specify file types to search through (again just read the page)

When calling the script, specify the directory in the first argument. It's usually easiest to go to the directory first and use a dot `.` to specify the current directory

``cleanser .``
