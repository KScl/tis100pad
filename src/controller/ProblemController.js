app.controller("ProblemController", ProblemController);


function ProblemController($scope, $http, $window, $location) {
    $scope.id = -1;
    $scope.solutions = 0;

    $scope.$watch('ordering', function(newValue, oldValue) {
        $location.search('order', newValue);

    });
    $scope.$watch('currentPage', function(newValue, oldValue) {
        $location.search('page', newValue);

    });


    $scope.init = function() {


        if ($location.$$search.page)
            $scope.currentPage = $location.$$search.page;
        else
            $scope.currentPage = 1;

        if ($location.$$search.order)
            $scope.ordering = $location.$$search.order
        else
            $scope.ordering = "INS"

        $scope.getPage()
    }

    $scope.getPage = function() {

        $http.post("/problem/solutionPage.json", {
            ordering: $scope.ordering,
            page: $scope.currentPage,
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