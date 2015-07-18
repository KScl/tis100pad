/**
TIS 100 Pad - 0.1.0
http://markgoodyear.com
Copyright (c) 2015 Mark Goodyear
License: MIT
*/
app.config(function($routeProvider,$locationProvider){$routeProvider.when("/:id",{controller:PadController}).when("/",{controller:PadController})});