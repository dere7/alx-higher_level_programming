#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];
request(url, function (err, res) {
  if (err) console.log(err);
  else {
    const film = JSON.parse(res.body);
    for (const characterUrl of film.characters) {
      request(characterUrl, function (err, res) {
        if (err) console.log(err);
        else {
          const character = JSON.parse(res.body);
          console.log(character.name);
        }
      });
    }
  }
});
