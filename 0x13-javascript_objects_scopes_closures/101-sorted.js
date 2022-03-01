#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  const val = dict[key];
  if (val in newDict) newDict[val].push(key);
  else newDict[val] = [key];
}
console.log(newDict);
