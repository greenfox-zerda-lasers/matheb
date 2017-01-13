(function(){
  var app = angular.module('store', []);
  //here we can define module, that works on index.html

  app.controller('StoreController', function(){
    this.products = gems;
  });

  var gems = [
    {
      name: 'Cat',
      description: 'A very short description',
      lovelyness: true,
      soldOut: true,
      img: 'cat.jpg'
    },
    {
      name: 'Dog',
      description: 'Similar to the first one',
      lovelyness: true,
      soldOut: true,
      img: 'dog.jpg'
    },
    {
      name: 'Travel',
      description: 'Far far away...',
      lovelyness: true,
      soldOut: true,
      img: 'travellers.jpg'
    },
    {
      name: 'Flying',
      description: 'Up in the air',
      lovelyness: true,
      soldOut: true,
      img: 'flying.jpg'
    },
  ];

})();
