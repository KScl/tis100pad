app.controller("ProblemController", ProblemController);


function ProblemController($scope, Upload, $http, $window, $location) {
    $scope.id = -1;
    $scope.solutions = 0;

    $scope.ordering = "INS";
    $scope.page = 1;


    $scope.init = function() {
        var page = 1;
        var order = "INS";

        if ($location.search.page)
            page = $location.search.page
        if ($location.search.order)
            order = $location.search.order
        $scope.getPage()
    }

    $scope.getPage = function() {

        $location.search("page", $scope.page);
        $location.search("order", $scope.ordering);

        $http.post("/problem/solutionPage.json", {
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


    $scope.submit = function() {

    }

};