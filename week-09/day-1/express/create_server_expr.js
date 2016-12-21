'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/:path', function post(req, resp) {
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1; // January is 0!
  var yyyy = today.getFullYear();

  if (dd < 10) {
    dd = '0' + dd;
  }

  if (mm < 10) {
    mm = '0' + mm;
  }

  today = mm + '/' + dd + '/' + yyyy;
  console.log('request was made: ', req.method, 'on path: ', req.url, 'at: ', today);
  var datas = 'request was made: '+ req.method + ' on path: /' + req.params.path + ' at: ' + today;
  resp.send(datas);
});

exampleApp.listen(3000);
