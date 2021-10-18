'use strict';

//Директива для валидации обязательных полей и отображения подсказки.

(function(){
	angular.module('avtoset.ui-controls')

	.directive('formSubmit', [
		function(){
			return {
				restrict: "A",
				link: function(scope, elm){
					elm.on('submit', function(){
						scope.$broadcast('formSubmit');
					})
				}
			}
		}
	])

	.directive('requiredField', [
		'$compile', '$timeout',
		function($compile, $timeout){
			return {
				restrict: "A",
				require: 'ngModel',
				// transclude: true,
				link: function(scope, elm, attr, ctrl) {
					if (!ctrl) return;

					var parentFormCtrl = elm.parent().controller('form');
					var parentFormCtrlName = parentFormCtrl.$name;
					var fieldName = attr["ngModel"].replace( /(\.\w)/g, g => g[1].toUpperCase());

					scope.$on('formSubmit', function(){
						scope.needShowErrors = true;
						scope.$apply();
					})

					attr.$set("name", fieldName);

					var el = angular.element('<div class="a-form-warning" ng-show="isShowError()">Поле не может быть пустым</div>');
					elm.parent().append(el);
					$compile(el)(scope);

					elm.bind('focus', function(){
						scope.elementLoosFocus = false;
						scope.$apply();
					})

					elm.bind('blur', function(){
						scope.elementLoosFocus = true;
						scope.$apply();
					})

					scope.isShowError = function() {
	                    if((scope.needShowErrors || scope.elementLoosFocus) && scope[parentFormCtrlName][fieldName].$error.requiredField) {
	                    	return true;
	                    }
	                    return false;
	                };

	                var validator = function(value) {
						if (_.has(attr, "requiredField") && ctrl.$isEmpty(value)) {
							ctrl.$setValidity('requiredField', false);
							return;
						} else {
							ctrl.$setValidity('requiredField', true);
							return value;
						}
					};

					ctrl.$formatters.push(validator);
					ctrl.$parsers.unshift(validator);
				}

			}
		}
	])
})()