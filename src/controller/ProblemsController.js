app.controller("ProblemsController", ProblemsController);

function ProblemsController($scope, $http, $window, $location) {
    $scope.problems = [];
    $scope.page = 1;
    $scope.problem_type = "OFFICIAL";
    $scope.total = 0;

    $scope.$watch('currentPage', function(newValue, oldValue) {
        $location.search('page', newValue);
    });

    $scope.getPage = function() {
        $location.search('type', $scope.problem_type);

        $http.post('/problem/problemPage.json', {
            page: $scope.currentPage,
            type: $scope.problem_type
        }).
        success(function(data, status, headers, config) {
            $scope.problems = data.result;
            $scope.total = data.count;
        });
    }

    $scope.init = function() {

        if ($location.search().page)
            $scope.currentPage = $location.search().page;
        else
            $scope.currentPage = 1;

        if($location.search().type)
            $scope.problem_type = $location.search().type;

        $scope.getPage();
    }

};