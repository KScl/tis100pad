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

    $scope.submit = function() {
        if ($scope.selected == "login") {

        } else {

            $http.post('/account/create.json', {
                name: $scope.account.name,
                password: $scope.account.password,
                repassword: $scope.account.repassword,
                captcha: $("#g-recaptcha-response").val()
            }).
            success(function(data, status, headers, config) {

            });

        }

    }

}