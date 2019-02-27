app.config(function($routeProvider, $locationProvider) {
    //configure the routing rules here
    $routeProvider.when('/:id', {
        templateUrl: 'pad.htmll',
        templateUrl: 'pad.html',
        controller: PadController
    }).when('/', {
        templateUrl: 'pad.html',
        controller: PadController
    });

});