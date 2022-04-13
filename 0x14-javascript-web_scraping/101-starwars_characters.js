#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];
request(url, function (err, res) {
  if (err) console.log(err);
  else {
    const film = JSON.parse(res.body);
    const characters = [];
    film.characters.forEach(function (characterUrl) {
      request(characterUrl, function (err, res) {
        if (err) console.log(err);
        else {
          const character = JSON.parse(res.body);
          characters.push(character.name);
        }
      });
    });
    characters.forEach(console.log);
  }
});
