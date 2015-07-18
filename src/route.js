app.config(function ($routeProvider, $locationProvider) {
    //configure the routing rules here
    $routeProvider.when('/:id', {
        controller: PadController
    })
    .when('/',{
        controller : PadController
    });
    
});