angular.module('events', ['eventService'])
.controller('eventController', ['$scope','$http', '$log', 'sharedEvent', function ($scope, $http, $log, sharedEvent) {
	/**
	 * Inicializar events
	 */
	$scope.events = {};
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

	$scope.event = sharedEvent;
	/**
	 * Muestra si hubo un error en el envío(false) o la confirmación (true)
	 */
	$scope.result_register = false;
	/**
	 * Muestra el resultado del envío
	 */
	$scope.finish_sending = false;
	/**
	 * Muestra mensaje de "se está enviadno"
	 */
	$scope.is_sending_register = false;
	/**
	 * Inicializar attendee
	 */
	$scope.attendee = {};
	$scope.attendee.id = "";
	/**
	 * For tests
	 */
	$scope.attendee.name = "Alberto";
	$scope.attendee.surname = "test2";
	$scope.attendee.email = "test2@gmail.com";
	$scope.attendee.web = "test2.com";
    $scope.submit = function(attendee,event) {
    	$scope.is_sending_register = true;
    	$scope.attendee = attendee;
    	$scope.attendee.event = event.id;
    	//attendee.event = event.id;
    	$http.post('api/attendees/', $scope.attendee)
            .success(function(data) {
            	console.log(data);
            	$scope.is_sending_register = false;
            	$scope.finish_sending = true;
            	$scope.result_register = data.result;
            	$scope.result_error_msg = data.error_msg;
            	$scope.attendee = data;
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
}]);