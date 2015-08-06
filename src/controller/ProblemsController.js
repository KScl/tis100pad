app.controller("ProblemsController", ProblemsController);

function ProblemsController($scope, Upload, $http, $window, $location) {
    $scope.problems = [];
    $scope.page = 1;

    $scope.getPage = function() {
        $location.search("page", $scope.page);

        $http.post('/problem/problemPage.json', {
            page: $scope.page
        }).
        success(function(data, status, headers, config) {
            $scope.problems = data.result;
        });
    }

    $scope.init = function() {
        var page = 1;
        if ($location.search().page)
        page = $location.search().page;

        $scope.page = page;
        $scope.getPage();
    }

};