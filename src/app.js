var app = angular.module('main', ['ngFileUpload', 'ngMessages']);

app.controller("loginController", loginController)

function loginController($scope, Upload, $http, $window, $location) {
    $scope.isLoginVisible = false;
    $scope.selected = "login";

    $scope.close = function() {
        $scope.isLoginVisible = false;
    }

    $scope.open = function() {
        $scope.isLoginVisible = true;
    }

}