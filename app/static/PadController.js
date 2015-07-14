
app.controller("PadController",PadController);

function PadController($scope) {

}

function resize()
{
    $(".node").each(function(index){
        var w = $(this).width();
        $(this).find(".node-block").each(function(){
            $(this).height(w);
        });
    });
}


    app.directive('resize', function ($window) {
        return function (scope, element) {
        var w = angular.element($window);
        scope.$watch(function () {
                return {
                    'h': w.height(), 
                    'w': w.width()
                };
            }, function (newValue, oldValue) {
resize();
        },true);

            w.bind('resize', function () {
                scope.$apply();
            });
        }
    });

    window.onload = function () { resize(); }



