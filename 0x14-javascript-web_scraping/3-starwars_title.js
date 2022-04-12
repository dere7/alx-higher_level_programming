#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];
request(url, function (err, res) {
  if (err) console.log(err);
  else {
    const json = JSON.parse(res.body);
    console.log(json.title);
  }
});
