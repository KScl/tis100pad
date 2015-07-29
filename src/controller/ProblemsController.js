app.controller("ProblemsController", ProblemsController);

function ProblemsController($scope, Upload, $http, $window, $location) {
    $scope.page = function(index) {
        window.location.pathname = "/problem/" + index;
    }

    $scope.select_problem = function(index) {
        window.location.pathname = "/problem/p/" + index;
    }
};