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

    OUTPUT = function() {
        this.data = null;
        this.result = null;
        this.process = function(data) {
            this.result = data;
            if (data == 1)
                this.data = {
                    name: "test",
                    data: {}
                };
            else if (data == 0)
                this.data = null;
            else
                this.data = JSON.stringify(eval("(" + data + ")"));
        }

        this.out = function() {
            if (this.data == null)
                return null;
            return this.data.name;
        }
        this.getClass = function() {
            if (this.data != null)
                return "active";
            return "";
        }
    }

    $scope.in = [{
        active: false
    }, {
        active: false
    }, {
        active: false
    }, {
        active: false
    }];
    $scope.out = [{
        active: false
    }, {
        active: false
    }, {
        active: false
    }, {
        active: false
    }];

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

    process = function(data) {
        if (data == 1)
            return {
                name: "test",
                data: {}
            };
        else if (data == 0)
            return null;
        else
            return JSON.stringify(eval("(" + data + ")"));
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
                    $scope.in[i] = process(data.inputs[i]);


                };

                for (var i = data.outputs.length - 1; i >= 0; i--) {
                    $scope.out[i] = process(data.outputs[i]);

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
                    $scope.in[i] = process(data.inputs[i]);

                };

                for (var i = data.outputs.length - 1; i >= 0; i--) {
                    $scope.out[i] = process(data.outputs[i]);

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
    //18 X 15 characters

    $scope.setState = function(node, state) {
        node.state = state;
    }

    $scope.save = function() {

        var out = {};
        if ($scope.id == -1) {
            var input = [];
            var output = [];

            for (var i = $scope.in.length - 1; i >= 0; i--) {
                input.push($scope.in[i]);
            };

            for (var i = $scope.out.length - 1; i >= 0; i--) {
                output.push($scope.out[i]);
            };

            out = {
                nodes: $scope.nodes,
                input: input,
                out: output
            };
        } else {
            out = {
                nodes: $scope.nodes,
                problemId: $scope.id
            };
        }

        $http.post('/pad/save.json', out).
        success(function(data, status, headers, config) {
            if (data.err) {
                $scope.errors = data.err;
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
        for (var x = 0; x < $scope.nodes.length; x++) {
            for (var y = 0; y < $scope.nodes[x].length; y++) {
                if ($scope.nodes[x][y].state == $scope.STATE.EXEC) {
                    index++;
                    output += "@" + (index - 1);
                    output += "\n";
                    output += $scope.nodes[x][y].text;

                    output += "\n"
                    output += "\n"
                }
            };
        };

        var anchor = angular.element('<a/>');
        anchor.attr({
            href: 'data:attachment/csv;charset=utf-8,' + encodeURI(output),
            target: '_blank',
            download: $scope.identifier + ".txt"
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
                        $scope.errors = data.err;
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


    $scope.changeSwitch = function(input) {
        if ($scope.id == -1) {
            input.active = !input.active;
        }

    }

}