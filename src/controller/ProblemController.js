app.controller("ProblemController", ProblemController);


function ProblemController($scope, Upload, $http, $window, $location) {
    $scope.id = -1;
    $scope.solutions = 0;
    $scope.ordering = "INS";
    $scope.page = 0;

    $scope.init = function() {
        $scope.getPage(0);
    }

    $scope.updateOrder = function(order) {
        $scope.ordering = order;
        $scope.getPage();
    }

    $scope.getPage = function() {

        $http.post("/problem/solutions.json", {
            ordering: $scope.ordering,
            page: $scope.page,
            problemId: $scope.id
        }).
        error(function(data, status, headers, config) {

        }).
        success(function(data, status, headers, config) {
            $scope.solutions = data.results;
        });
    }


    $scope.submit = function() {}

};