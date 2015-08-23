# tis100pad

[![Stories in Ready](https://badge.waffle.io/pollend/tis100pad.svg?label=ready&title=Ready)](http://waffle.io/pollend/tis100pad)

A web site for uploading and sharing solutions for the game TIS-100. http://www.tis100pad.com

##Feature
* A user account system
* Anonmous user or registerd user can submit solution
* Registered user can submit problems
* Both solutions and problems can be reviewied by Anonmous/Registed users and resaved as seperate entries

##Installing

###Required Libraries

npm libraries

```
npm install -g grunt-cli
npm install -g bower
```

pip libraries

```
pip install flask
pip install flask-sqlalchemy
pip install Flask-KVSession
pip install Redis
pip install requests
pip install lupa
pip install psutil
```

###Install

```
npm install
bower install
grunt build
grunt migrate
```


##Modifying

```
grunt wtch
```

grunt will watch the src directory for any changes and rebuild the the project accordingly. Flask will restart with any changes to to the base server files but may occasionally crash with syntax errors.

```
grunt clean-up-bin
```

This command will clear the build directory file.

