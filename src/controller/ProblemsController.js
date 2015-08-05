app.controller("ProblemsController", ProblemsController);

function ProblemsController($scope, Upload, $http, $window, $location) {
    $scope.problems = [];
    $scope.getPage = function(page) {
        $http.post('/problem/page.json', {
            page: page
        }).
        success(function(data, status, headers, config) {
            $scope.problems = data.result;
        });
    }


};