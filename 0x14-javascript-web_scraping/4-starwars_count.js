#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (err, res) {
  if (err) console.log(err);
  else {
    const films = JSON.parse(res.body);
    let count = 0;
    for (const film of films.results) {
      if (film.characters.includes(wedge)) {
        count++;
      }
    }
    console.log(count);
  }
});
