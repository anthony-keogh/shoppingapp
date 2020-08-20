
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.count = 0;
});

app.controller('myCtrl', function($scope) {
    $scope.count2 = 0;
});

var app = angular.module('myApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});



$('.likebutton').click(function(){
    
$.ajax(
    {
        type:"GET",
        url: "/likeproduct",
        dataType:'json',
        success: function(data) 
        {
          console.log(JSON.stringify(data))  
        },
        error: function(request, status, error){
            console.log("Error:"+ error)
        }
     });
});


