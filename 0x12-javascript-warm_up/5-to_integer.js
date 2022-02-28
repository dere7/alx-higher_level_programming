#!/usr/bin/node
let number;
if ( (number = parseInt(process.argv[2])))
  console.log('My number: ', number);
else console.log('Not number');
