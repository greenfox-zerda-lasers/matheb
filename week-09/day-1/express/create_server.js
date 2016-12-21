'use strict';

var http = require('http');

var server = http.createServer(function get(req, res) {
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth()+1; //January is 0!
  var yyyy = today.getFullYear();

  if(dd<10) {
    dd='0'+dd
  }

  if(mm<10) {
    mm='0'+mm
  }

  today = mm+'/'+dd+'/'+yyyy;
  console.log('request was made: ', req.method, 'on path: ', req.url, 'at: ', today);
  var datas = 'request was made: ' + req.method + ' on path: ' + req.url + ' at: ' + today;
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end(datas);
});


server.listen(3000, '127.0.0.1');
