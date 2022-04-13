#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

request(argv[2], function (err, res) {
  if (err) console.log(err);
  else console.log('code:', res.statusCode);
});
