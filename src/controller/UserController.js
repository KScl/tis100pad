app.controller("UserController", UserController);

function UserController($scope, $http, $window, $location) {
    $scope.IsPassword = true;
    $scope.problem_page = 1;
    $scope.solution_page  = 1;
    $scope.state = 'submitted_problem';
    $scope.solution_ordering = "INS";
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

    $scope.show_solution_items = function(problem,toggle){
        if(typeof problem.ordering === 'undefined')
            problem.ordering = 'CYL';

        if(toggle)
        {
            if(problem.show  === true)
                problem.show = false;
            else
                problem.show = true;
        }

        $http.post("/user/solution_list.json", {
            user: $scope.user,
            problem_id: problem.id,
            ordering : problem.ordering
        }).
        error(function(data, status, headers, config) {

        }).
        success(function(data, status, headers, config) {
            problem.items = data.results;
            problem.page = data.page;
        });
        
    }

    $scope.$watch('state', function(newValue, oldValue) {
        $location.search('state', newValue);
        if (newValue == 'profile') {
            delete $location.$$search.order

        } else if (newValue == 'submitted_problem') {
             delete $location.$$search.order
             $scope.update_problems();

        } else if (newValue == 'submitted_solution') {
            
            $scope.update_solutions();
        }
    });


    $scope.$watch('solution_ordering', function(newValue, oldValue) {
        $location.search('order', newValue);
        $scope.update_solutions();
    });

    $scope.update_problems = function(){
        $location.search('page', $scope.problem_page);
        $http.post("/user/problemsPage.json", {
            page: $scope.problem_page,
            user: $scope.user
        }).
        error(function(data, status, headers, config) {

        }).
        success(function(data, status, headers, config) {
            $scope.submitted_problems = data.results;
            $scope.submitted_problems_total = data.total;
        });
    }

    $scope.update_solutions = function() {
       $location.search('page', $scope.solution_page);
        $http.post("/user/solutionPage.json", {
            page: $scope.solution_page,
            user: $scope.user,
            ordering: $scope.solution_ordering
        }).
        error(function(data, status, headers, config) {

        }).
        success(function(data, status, headers, config) {
            $scope.problems_solutions = data.results;
            $scope.problems_solutions_total = data.total;
        });

    }

    $scope.init = function() {

        if ($location.$$search.state)
            $scope.state = $location.$$search.state;
        else
            $scope.state = 'profile';

        if ($scope.state = 'profile' && !$scope.owner)
            $scope.state = 'submitted_solution';

        if($location.$$search.state)
        {
            $scope.state = $location.$$search.state;

            if ($scope.state == "submitted_problem")
            {
                $scope.problem_page = $location.$$search.page;
            }
            if($scope.state == "submitted_solution")
            {
                if ($location.$$search.order)
                     $scope.solution_ordering = $location.$$search.order
                $scope.solution_page = $location.$$search.page;
            }
        }
        
    }


    $scope.$watch('state', function(newValue, oldValue) {
        $location.search('state', newValue);
    });


};