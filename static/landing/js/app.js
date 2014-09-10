var app = angular.module('eventApp', ['ngRoute', 'ngResource', 'events', 'formAttendee']);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});