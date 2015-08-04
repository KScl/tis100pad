app.controller("loginController", loginController)
    .directive('match', function() {
        return {
            restrict: 'A',
            require: 'ngModel',
            link: function(scope, element, attr, ctrl) {
                ctrl.$validators.match = function(modelValue, viewValue) {

                    if (scope.NewAccount.repeatPassword == null || scope.NewAccount.repeatPassword == "") {
                        // consider empty models to be valid
                        return true;
                    }
                    return scope.NewAccount.repeatPassword == viewValue;
                };

            }
        }
    }).directive("verify", function($q, $timeout, $http) {
        return {
            restrict: 'A',
            require: 'ngModel',
            link: function(scope, element, attr, ctrl) {
                ctrl.$asyncValidators.verify = function(modelValue, viewValue) {
                    console.log(viewValue)
                    var def = $q.defer();
                    $http.post('/account/nameCheck.json', {
                        name: viewValue
                    }).success(function(data, status, headers, config) {
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

function loginController($scope, Upload, $http, $window, $location) {
    $scope.isLoginVisible = false;
    $scope.selected = "login";

    $scope.$watch("NewAccount.repeatPassword", function() {
        $scope.NewAccount.Password.$validate();
    })

    $scope.close = function() {
        $scope.isLoginVisible = false;
    }

    $scope.open = function() {
        $scope.isLoginVisible = true;
    }


    $scope.createNewAccount = function() {
        console.log($scope.getRecaptchaResponse())
        if ($scope.NewAccount.$valid) {
            $http.post('/account/create.json', {
                name: $scope.NewAccount.name,
                password: $scope.NewAccount.password,
                captcha: $scope.getRecaptchaResponse()
            }).
            success(function(data, status, headers, config) {

            });
        }
    }

    $scope.getRecaptchaResponse = function() {
        return grecaptcha.getResponse();
    }





}