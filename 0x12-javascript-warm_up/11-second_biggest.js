#!/usr/bin/node
argv = process.argv.slice(2)
  .map(val => parseInt(val))
  .sort();
console.log(argv[argv.length - 2] || 0);
