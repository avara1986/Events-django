angular.module('events', ['eventService'])
.controller('eventController', ['$scope','$http', '$log', 'sharedEvent', function ($scope, $http, $log, sharedEvent) {
	$scope.events = [];
	$http.get('/api/events/').
    success(function(data, status, headers, config) {
        $scope.events = data;
        console.log($scope.events);
      }).
      error(function(data, status, headers, config) {
        console.log(data);
        console.log(status);
        console.log(headers);
        console.log(config);
      });
	  $scope.setRegisterEvent = function(id, title) {
		  sharedEvent.id = id;
		  sharedEvent.title = title;
	  };
}]);

angular.module('formAttendee', [])
.controller('attendeeController', ['$scope','$http', '$log' , 'sharedEvent', function($scope, $http, $log, sharedEvent) {
	$scope.form = {};
	$scope.event = sharedEvent;
	$scope.result_register = false;
	$scope.is_sending_register = false;
	$scope.attendee_id = "";
    $scope.submit = function(attendee,event) {
    	$scope.is_sending_register = true;
        //var in_data = { subject: $scope.subject };
    	attendee.event = event.id;
    	//attendee.id = '1';
    	//console.log(attendee);
    	$http.post('api/attendees/', attendee)
            .success(function(data) {
            	$scope.is_sending_register = false;
            	console.log(data);
            	$scope.attendee_id = data.id;
            	$scope.result_register = true;
            }).
            error(function(data, status, headers, config) {
                console.log(data);
                console.log(status);
                console.log(headers);
                console.log(config);
            });
    }
	$scope.reset = function() {
		$scope.attendee = angular.copy($scope.master);
	};
	
	$scope.reset();
}]);