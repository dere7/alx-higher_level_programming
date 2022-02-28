#!/usr/bin/node
let argv = process.argv.slice(2);
argv = argv.map(val => parseInt(val));
argv.sort((a, b) => a - b);
console.log(argv[argv.length - 2] || 0);
