# tis100pad

A web site for uploading and sharing solutions for the game TIS-100. http://www.tis100pad.com

##Installing

```
sudo npm -g install grunt-cli bower
npm install
bower install
grunt build
```
grunt will minify the javascript, and move source files from src to bin. first run the the shell.py file, this will create the tables for the server. then run the run.py to actually run the server.

##Modifying

```
grunt wtch
```

This will watch src directory for any changes and rebuild the the project accordingly. python will have to be run seperely in a seperate command window. Flask will restart with any changes to to the base server files but may occasionally crash with syntax errors. 

```
grunt cln
```

This command will clear the source directory file.
