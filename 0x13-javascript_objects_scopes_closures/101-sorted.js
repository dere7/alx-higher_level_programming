#!/usr/bin/node

const dict = require('./101-dict').dict;
const uniqueKeys = [];
const occurrence = {};
Object.values(dict).forEach(val => {
  if (!(val in uniqueKeys)) uniqueKeys.push(val);
});
uniqueKeys.sort().forEach(val => {
  occurrence[val] = [];
  for (const key in dict) {
    if (dict[key] === val) occurrence[val].push(key);
  }
});
console.log(occurrence);
