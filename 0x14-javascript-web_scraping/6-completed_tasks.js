#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = argv[2];
request(url, function (err, res) {
  if (err) console.log(err);
  else {
    const todos = JSON.parse(res.body).filter(function (todo) {
      return todo.completed;
    });
    const completed = {};
    for (const todo of todos) {
      if (completed[todo.userId]) {
        completed[todo.userId]++;
      } else {
        completed[todo.userId] = 1;
      }
    }
    console.log(completed);
  }
});
