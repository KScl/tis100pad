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

    $scope.download_problem = function(identifier) {
        var anchor = angular.element('<a/>');

        $http.get("/problem/p/download/" + identifier).
        error(function(data, status, headers, config) {

        }).
        success(function(data, status, headers, config) {
            anchor.attr({
                 href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
                target: '_blank',
                download: identifier + ".txt"
            })[0].click();
        });

    }

    $scope.upload_save = function(files) {
        FileAPI.readAsText(files[0], function(evt) {
            //$scope.new_solution();
            if (evt.type == 'load') {
                var identifier = files[0].name.substring(0, files[0].name.indexOf("."));
                if ($scope.identifier == identifier) {
                    $http.post("/pad/problem.json", {
                        identifier: identifier,
                        file: evt.result
                    }).
                    error(function(data, status, headers, config) {

                    }).
                    success(function(data, status, headers, config) {
                        if (data.result) {
                            $location.search("id", data.id);
                            $scope.id = data.id;
                            $scope.init();
                        } else {
                            $scope.sideError = data.errors
                            //window.location.pathname = "/pad/" + data.id;
                        }
                    });
                } else {
                    $scope.sideError = [{
                        'type': 'danger',
                        'out': "Identifiers don't match"
                    }];
                }
                return false;
            } else if (evt.type == 'progress') {
                var pr = evt.loaded / evt.total * 100;
            } else {
                // Error
            }
        });

    }


    $scope.submit = function() {

    }

};