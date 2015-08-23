app.controller("ProblemsController", ProblemsController);

function ProblemsController($scope, $http, $window, $location) {
    $scope.problems = [];
    $scope.page = 1;

    $scope.$watch('currentPage', function(newValue, oldValue) {
        $location.search('page', newValue);
    });

    $scope.getPage = function() {

        $http.post('/problem/problemPage.json', {
            page: $scope.currentPage
        }).
        success(function(data, status, headers, config) {
            $scope.problems = data.result;
        });
    }

    $scope.init = function() {

        if ($location.search().page)
            $scope.currentPage = $location.search().page;
        else
            $scope.currentPage = 1;
        $scope.getPage();
    }

};