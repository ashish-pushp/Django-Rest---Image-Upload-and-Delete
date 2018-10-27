"use strict";

var myApp = angular.module('imageuploadFrontendApp', [
    'ngResource',
    'ngFileUpload',
    'ngAnimate',
    'toaster'
]);

myApp.config(function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller('MainCtrl', function($scope, Images, toaster)
{
    console.log('In main Control');

    $scope.images = [];

    $scope.newImage = {};
    $scope.imagesLoading = false;
    $scope.loadImages = function() {
        $scope.imagesLoading = true;

        return Images.query().$promise.then(
            function success(response) {
                $scope.images = response;
                $scope.imagesLoading = false;

                return response;
            },
            function error(rejection) {
                console.log(rejection);
                $scope.imagesLoading = false;
                return rejection;
            }
        );
    };
    $scope.uploadImage = function()
    {
        Images.save($scope.newImage).$promise.then(
            function(response) {
                $scope.images.unshift(response);
                $scope.newImage = {};

                toaster.pop('success', "Image uploaded!");
            },
            function(rejection) {
                console.log('Failed to upload image');
                console.log(rejection);
                toaster.pop('error', "Failed to upload image");
            }
        );
    };

    $scope.deleteImage = function(image)
    {
        image.$delete(
            function(response)
            {
                console.log('Deleted it');
                var idx = $scope.images.indexOf(image);
                if (idx < 0) {
                    console.log('Error: Could not find image');
                } else {
                    $scope.images.splice(idx, 1);
                }

                toaster.pop('success', "Image deleted");
            },
            function(rejection)
            {
                console.log('Failed to delete image');
                console.log(rejection);
                toaster.pop('error', "Failed to delete image");
            }
        );
    };

    $scope.loadImages();
});


