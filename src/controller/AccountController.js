app.controller("loginController", loginController).directive("verifyIdentity", function($q, $timeout, $http) {
    return {
        restrict: 'A',
        require: 'ngModel',
        link: function(scope, element, attr, ctrl) {
            ctrl.$asyncValidators.verifyIdentity = function(modelValue, viewValue) {
                var def = $q.defer();
                $http.post('/account/nameCheck.json', {
                    name: viewValue
                }).success(function(data, status, headers, config) {
                    console.log(data.result)
                    if (data.result == true) {
                        def.resolve();
                    } else {
                        def.reject();
                    }
                });
                return def.promise;
            };
        }
    }
})

function loginController($scope, $http, $window, $location) {
    $scope.isLoginVisible = false;
    $scope.selected = "login";
    $scope.username = "";
    $scope.newAccountAlerts = [];
    $scope.loginAlerts = [];
    $scope.IsPassword = false;

    $scope.checkPasswords = function() {
        if ($scope.NewAccount.repeatPassword == $scope.NewAccount.password) {
            $scope.IsPassword = true;
            return true;
        }
        $scope.IsPassword = false;
        return false;
    }



    $scope.close = function() {
        $scope.isLoginVisible = false;
    }

    $scope.open = function() {
        $scope.isLoginVisible = true;
    }

    $scope.verifySession = function() {
        $http.post("/account/verify.json", {})
            .success(function(data, status, headers, config) {
                if (data.result == true) {
                    $scope.username = data.name;
                    $scope.close();
                } else {
                    $scope.username = "";
                }
            });
    }

    $scope.createNewAccount = function() {
        if ($scope.checkPasswords()) {
            if ($scope.NewAccount.$valid) {
                $http.post('/account/create.json', {
                    name: $scope.NewAccount.name,
                    password: $scope.NewAccount.password,
                    captcha: $scope.getRecaptchaResponse()
                }).
                success(function(data, status, headers, config) {
                    $scope.NewAccount.output = data.output;

                    if (data.result == true) {
                        $scope.verifySession();
                        $scope.close();
                    }
                });
            }
        }
    }

    $scope.accountLogin = function() {
        if ($scope.Login.$valid) {
            $http.post('/account/login.json', {
                name: $scope.login.name,
                password: $scope.login.password,
            }).
            success(function(data, status, headers, config) {
                $scope.login.output = data.output;
                if (data.result == true) {
                    $scope.verifySession();
                }
            });
        }

    }

    $scope.logout = function() {
        $http.post('/account/logout.json', {}).
        success(function(data, status, headers, config) {
            $scope.verifySession();
        });
    }

    $scope.getRecaptchaResponse = function() {
        return grecaptcha.getResponse();
    }

}
