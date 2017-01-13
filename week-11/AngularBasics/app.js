(function(){
  var app = angular.module('store', []);
  //here we can define module, that works on index.html

  app.controller('StoreController', function(){
    this.products = gems;
  });

  var gems = [
    {
      name: 'D',
      price: 2.95,
      description: 'A very short description',
      canPurchase: true,
      soldOut: true,
    },
    {
      name: 'B',
      price: 4.50,
      description: 'Similar to the first one',
      canPurchase: true,
      soldOut: true,
    },
  ];

})();
