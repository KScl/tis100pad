app.controller("UserController", UserController);

function UserController($scope, Upload, $http, $window, $location) {
    $scope.IsPassword = true;

    $scope.passwordCheck = function() {
        if ($scope.ChangePassword.newPassword == $scope.ChangePassword.repeatPassword) {
            $scope.IsPassword = true;
            return true;
        }
        $scope.IsPassword = false;
        return false;
    }

    $scope.changePassword = function() {
        if ($scope.passwordCheck()) {
            if ($scope.ChangePassword.$valid) {
                $http.post("/user/changePassword.json", {
                    oldPassword: $scope.ChangePassword.oldPassword,
                    newPassword: $scope.ChangePassword.newPassword
                }).
                error(function(data, status, headers, config) {

                }).
                success(function(data, status, headers, config) {
                    $scope.ChangePassword.output = data.output;
                });

            }
        }
    }

    $scope.$watch('state', function(newValue, oldValue) {
        $location.search('state', newValue);
        $scope.currentPage = 1;

        if (newValue == 'profile') {
            delete $location.$$search.order

        } else if (newValue == 'submitted_problem') {
            delete $location.$$search.order

        } else if (newValue == 'submitted_solution') {
            $scope.update_solutions();
        }
    });


    $scope.$watch('ordering', function(newValue, oldValue) {
        $location.search('order', newValue);
        $scope.update_solutions();
    });

    $scope.update_solutions = function() {
        $http.post("/user/solutionPage.json", {
            ordering: $scope.ordering,
            page: $scope.currentPage,
            user: $scope.user
        }).
        error(function(data, status, headers, config) {

        }).
        success(function(data, status, headers, config) {
            $scope.solutions = data.results;
        });

    }

    $scope.init = function() {

        if ($location.$$search.page)
            $scope.currentPage = $location.$$search.page;
        else
            $scope.currentPage = 1;

        if ($location.$$search.order)
            $scope.ordering = $location.$$search.order
        else
            $scope.ordering = "INS"

        if ($scope.user)
            $scope.state = 'submitted_problem';

        if ($location.$$search.state)
            $scope.state = $location.$$search.state;
        else
            $scope.state = 'profile';

        if ($scope.state = 'profile' && !$scope.owner)
            $scope.state = 'submitted_solution';
    }


    $scope.$watch('state', function(newValue, oldValue) {
        $location.search('state', newValue);
    });


};