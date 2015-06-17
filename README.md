# tis100pad
A web site for uploading and sharing solutions for the game TIS-100. http://www.tis100pad.com

If you attempt to run this site on your own server, you can put the .py files anywhere as long as your web server is able to execute them. Needless to say I recommend putting them somewhere externally inaccessible.

I myself am using mod_wsgi on an Apache server, but it should work fine with any server setup that can run Flask apps, so long as the appropriate POST requests are correctly routed to the app.

You would also need to initialize your own SQLite database with table, as the code in this repo does not do this for you. Schema: `CREATE TABLE solutions (master int, forkno int, "@0" text, "@1" text, "@2" text, "@3" text, "@4" text, "@5" text, "@6" text, "@7" text, "@8" text, "@9" text, "@10" text, "@11" text, ports text, levelcode text)`
