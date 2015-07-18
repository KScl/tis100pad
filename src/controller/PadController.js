app.controller("PadController", PadController);

function PadController($scope,Upload, $http,$window,$location,$routeParams) {

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

    $scope.$on('$routeChangeSuccess', function () {
        console.log($routeParams.id);

        if($routeParams.id)
        {
            $http.post('/solution/' +  $routeParams.id, {}).
            success(function(data, status, headers, config) {
                for (var x = $scope.nodes.length - 1; x >= 0; x--) {
                   for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {

                       $scope.nodes[x][y].text = data.solution[x][y];
                   };
                   
                };
            }).
            error(function(data, status, headers, config) {

            });
        } 
        else
        {
             for (var x = $scope.nodes.length - 1; x >= 0; x--) {
          for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
              $scope.nodes[x][y].text = "";
          };
       };
        }   

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
            

            $location.path(data.id);


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
                output += "@"+index;
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
        $location.path("");
     for (var x = $scope.nodes.length - 1; x >= 0; x--) {
          for (var y = $scope.nodes[x].length - 1; y >= 0; y--) {
              $scope.nodes[x][y].text = "";
          };
       };
    }

  $scope.$watch('upload_file', function () {
    if($scope.upload_file)
        $scope.upload_save($scope.upload_file);
    });

    $scope.upload_save = function (files) {
        FileAPI.readAsText(files[0], function (evt){
            $scope.new_solution();

            if( evt.type == 'load' )
            {
                var lines = evt.result.split('\n');
                for (var i = 0; i < lines.length; i++) 
                {
                    if(lines[i].trim().substring(0,1) == "@")
                    {
                         var index =  parseInt(lines[i].trim().substring(1));
                         i++;
                        
                        for (; i < lines.length; i++) 
                        {
                           
                             if(lines[i].trim().substring(0,1) == "@")
                            {
                                i--;
                                break;
                            }
                            else
                            {
                                  $scope.nodes[Math.ceil((index+1)/4)-1][(index%3)].text += lines[i];
                            }
                        }
                        $scope.nodes[Math.ceil((index+1)/4)-1][(index%3)].text = $scope.nodes[Math.ceil((index+1)/4)-1][(index%3)].text.trim();

                    }
                };
                $scope.save();
            } else if( evt.type =='progress' ){
                var pr = evt.loaded/evt.total * 100;
            } else {
                // Error
            }
        });
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