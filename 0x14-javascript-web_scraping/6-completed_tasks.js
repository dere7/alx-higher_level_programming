#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = argv[2] + '?completed=true';
let users = 'https://jsonplaceholder.typicode.com/users';
request(url, function (err, res) {
  if (err) console.log(err);
  else {
    const todos = JSON.parse(res.body);
    console.log(todos);
    const completed = {};
    // for (const user of users) {
    //   users += '/' + user.id + '/todos/?completed=true';
    //   request(users, function (err, res) {
    //     if (err) console.log(err);
    //     else {
    //       // let json = JSON.parse(res.body);
    //       // console.log(json);
    //       // completed[user.id] =json.length;
    //     }
    //   });
    // }
    console.log(completed);
  }
});
