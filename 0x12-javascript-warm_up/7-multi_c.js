#!/usr/bin/node
let number;
if ((number = parseInt(process.argv[2]))) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
