app.controller("PadController", PadController);


function PadController($scope, $http,$window) {

    $scope.STATE = {
        EXEC: 0,
        STCK: 1,
        ERR: 3
    }
    $scope.nodes = [
        [{
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }],
        [{
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }],
        [{
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }, {
            state: $scope.STATE.EXEC,
            text: ""
        }]
    ]

    angular.element(document).ready(function () {
        $http.post('/solution/' +  $scope.solutionId, {}).
        success(function(data, status, headers, config) {
            for (var x = $scope.nodes.length - 1; x >= 0; x--) {
               for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {

                   $scope.nodes[x][y].text = data.solution[x][y];
               };
               
            };
        }).
        error(function(data, status, headers, config) {

        });
    });


    $scope.getClass = function(node) {
        if (node) {
            if (node.state === $scope.STATE.EXEC) {
                return "execnode";
            }
            if (node.state === $scope.STATE.STCK) {
                return "stcknode";
            }
            if (node.state === $scope.STATE.ERR) {
                return "errnode";
            }
        }

    }



    $scope.setState = function(node, state) {
        node.state = state;
    }

    $scope.save = function() {
        $http.post('/save', {
            nodes: $scope.nodes
        }).
        success(function(data, status, headers, config) {
            $window.location.href =  data.id;

        }).
        error(function(data, status, headers, config) {

        });
    }

    $scope.download = function() {
        $http.post('/download',{
            nodes : $scope.nodes
        }).
        success(function(data, status, headers, config) {
             var anchor = angular.element('<a/>');
             anchor.attr({
                 href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
                 target: '_blank',
                 download: 'soltuon.txt'
             })[0].click();

        }).
        error(function(data, status, headers, config) {

        });
    }

    $scope.upload_save = function() {

    }

    $scope.new_solution = function() {

    }

}

function resize() {
    $(".node").each(function(index) {
        var w = $(this).width();
        $(this).find(".node-block").each(function() {
            $(this).height(w);
        });
    });
}


app.directive('resize', function($window) {
    return function(scope, element) {
        var w = angular.element($window);
        scope.$watch(function() {
            return {
                'h': w.height(),
                'w': w.width()
            };
        }, function(newValue, oldValue) {
            resize();
        }, true);

        w.bind('resize', function() {
            scope.$apply();
        });
    }
});

window.onload = function() {
    resize();
}