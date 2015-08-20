app.controller("PadController", PadController).directive('resize', function($window) {
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

function resize() {
    $(".node").each(function(index) {
        var w = $(this).width();
        $(this).find(".node-block").each(function() {
            $(this).height(w);
        });
    });
}

function PadController($scope, Upload, $http, $window, $location) {

    window.onload = function() {
        resize();
    }

    $scope.STATE = {
        EXEC: 0,
        STCK: 1,
        ERR: 2
    }

    $scope.problem = "";
    INPUT = function() {
        this.active = false;
        this.name = "";
        this.out = function() {
            return "." + this.name;
        }
        this.getClass = function() {
            if (this.active)
                return "active";
            return "";
        }
    }

    OUTPUT = function() {
        this.active = false;
        this.name = "";
        this.out = function() {
            return "." + this.name;
        }
        this.getClass = function() {
            if (this.active)
                return "active";
            return "";
        }
    }

    $scope.in = [
        new INPUT(), new INPUT(), new INPUT(), new INPUT()
    ];

    $scope.out = [
        new OUTPUT(), new OUTPUT(), new OUTPUT(), new OUTPUT()
    ];

    NODE = function() {
        this.state = $scope.STATE.EXEC;
        this.text = "";
    }

    $scope.nodes = [
        [new NODE(), new NODE(), new NODE(), new NODE()],
        [new NODE(), new NODE(), new NODE(), new NODE()],
        [new NODE(), new NODE(), new NODE(), new NODE()]
    ];
    $scope.user = '';
    $scope.id = -1;
    $scope.identifier = "";
    $scope.name = "";
    $scope.errors = [];



    $scope.cycleCount = 0;
    $scope.nodeCount = 0;
    $scope.instructionCount = 0;

    $scope.updateCount = function() {
        $scope.cycleCount = 0;
        $scope.nodeCount = 0;
        $scope.instructionCount = 0;

        for (var x = $scope.nodes.length - 1; x >= 0; x--) {
            for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
                if ($scope.nodes[x][y].text.trim() !== "") {
                    $scope.nodeCount++;
                }

                var lines = $scope.nodes[x][y].text.trim().split(/\r\n|\r|\n/g);
                for (var i = lines.length - 1; i >= 0; i--) {

                    if (!(lines[i].trim() == "" || lines[i].trim().substring(0, 1) == "#")) {
                        $scope.instructionCount++;
                    }
                };
            };

        };
    }

    $scope.init = function() {
        if ($location.search().id && $location.search().id >= 0) {
            $scope.id = $location.search().id;

            $http.post('/pad/solution/' + $scope.id, {}).
            success(function(data, status, headers, config) {
                $scope.user = data.user
                for (var x = $scope.nodes.length - 1; x >= 0; x--) {
                    for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
                        $scope.nodes[x][y].text = data.grid[x][y];
                        $scope.nodes[x][y].state = data.states[x][y];

                    };
                };
                $scope.id = data.problemId;
                $scope.identifier = data.identifier;
                $scope.name = data.name;

                for (var i = data.inputs.length - 1; i >= 0; i--) {
                    if (data.inputs[i] != null)
                        $scope.in[i].active = true;
                    else
                        $scope.in[i].active = false;

                };

                for (var i = data.outputs.length - 1; i >= 0; i--) {
                    if (data.outputs[i] != null)
                        $scope.out[i].active = true;
                    else
                        $scope.out[i].active = false;

                };

                $scope.updateCount();
            }).
            error(function(data, status, headers, config) {

            });
        } else if ($location.search().problem) {
            $http.post('/pad/problem/' + $location.search().problem, {}).
            success(function(data, status, headers, config) {
                for (var x = $scope.nodes.length - 1; x >= 0; x--) {
                    for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
                        $scope.nodes[x][y].state = data.states[x][y];

                    };
                };
                $scope.id = data.problemId;
                $scope.identifier = data.identifier;
                $scope.name = data.name;

                for (var i = data.inputs.length - 1; i >= 0; i--) {
                    if (data.inputs[i] != null)
                        $scope.in[i].active = true;
                    else
                        $scope.in[i].active = false;

                };

                for (var i = data.outputs.length - 1; i >= 0; i--) {
                    if (data.outputs[i] != null)
                        $scope.out[i].active = true;
                    else
                        $scope.out[i].active = false;

                };

            });

        } else {
            for (var x = $scope.nodes.length - 1; x >= 0; x--) {
                for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
                    $scope.nodes[x][y].text = "";
                };
            };
        }
    }



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
        $http.post('/pad/save.json', {
            nodes: $scope.nodes,
            problemId: $scope.id,
            input: $scope.in,
            out: $scope.out
        }).
        success(function(data, status, headers, config) {
            if (data.errors) {
                $scope.errors = data.errors;
            } else {
                $location.search("id", data.id);
                $scope.id = data.id;
                $scope.init();
            }
        }).
        error(function(data, status, headers, config) {

        });
    }

    $scope.download = function() {
        var output = "";
        var index = 0;
        for (var x = $scope.nodes.length - 1; x >= 0; x--) {
            for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
                index++;
                output += "@" + index;
                output += $scope.nodes[x][y].text;

                output += "\n"
            };
        };

        var anchor = angular.element('<a/>');
        anchor.attr({
            href: 'data:attachment/csv;charset=utf-8,' + encodeURI(output),
            target: '_blank',
            download: 'soltuon.txt'
        })[0].click();

    }

    $scope.new_solution = function() {
        //window.location.pathname = "/pad/";
        for (var x = $scope.nodes.length - 1; x >= 0; x--) {
            for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
                $scope.nodes[x][y].text = "";
            };
        };
    }

    /*$scope.$watch('upload_file', function() {
        if ($scope.upload_file)
            $scope.upload_save($scope.upload_file);
    });*/



    $scope.upload_save = function(files) {
        FileAPI.readAsText(files[0], function(evt) {
            //$scope.new_solution();
            if (evt.type == 'load') {

                var identifier = files[0].name.substring(0, files[0].name.indexOf("."));

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
                        $scope.upload_errors = data.errors

                        //window.location.pathname = "/pad/" + data.id;
                    }
                });
                return false;
            } else if (evt.type == 'progress') {
                var pr = evt.loaded / evt.total * 100;
            } else {
                // Error
            }
        });

    }

}