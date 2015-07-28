app.controller("ProblemsController", ProblemsController).directive('resize', function($window) {
    return function(scope, element) {
        var w = angular.element($window);
        scope.$watch(function() {
            return {
                'h': w.height(),
                'w': w.width()
            };
        }, function(newValue, oldValue) {
            resize();
        }, true);

        w.bind('resize', function() {
            scope.$apply();
        });

    }
});


function resize() {

}


function ProblemsController($scope, Upload, $http, $window, $location) {
    $scope.page = function(index) {
        window.location.pathname = "/problems/" + index;
    }

};