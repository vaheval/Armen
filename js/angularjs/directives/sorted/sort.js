
function Controller($scope) {
  $scope.order = 'name';
  $scope.reverse = false;
    

  $scope.friends = [
    {name:'John', phone:'555-1212', age:10},
    {name:'Mary', phone:'555-9876', age:19},
    {name:'Mike', phone:'555-4321', age:21},
    {name:'Adam', phone:'555-5678', age:35},
    {name:'Julie', phone:'555-8765', age:29}]; 
}

angular.module('myApp', []).directive("sort", 
    function () {
        return {
            restrict: 'A',
            transclude: true,
            template :
              '<div class="pointer" ng-click="onClick()">'+
                '<span ng-transclude></span>'+
                '<i ng-if="order === by && !reverse" style="margin-left: 5px;" class="fas fa-long-arrow-alt-down"></i>'+
                '<i ng-if="order === by && reverse" style="margin-left: 5px;" class="fas fa-long-arrow-alt-up"></i>'+
              '</div>',
            scope: {
                order: '=',
                by: '=',
                reverse : '='
            },
            link: function(scope, element, attrs) {
                scope.onClick = function () {
                    if( scope.order === scope.by ) {
                        scope.reverse = !scope.reverse;
                    } else {
                        scope.by = scope.order ;
                        scope.reverse = false;
                    }
                }
            }
        }
    },
);
