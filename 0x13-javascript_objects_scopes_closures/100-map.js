#!/usr/bin/node

let list = require('./100-data').list;
console.log(list);
list = list.map((val, i) => val * i);
console.log(list);
