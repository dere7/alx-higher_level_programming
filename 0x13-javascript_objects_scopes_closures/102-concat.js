#!/usr/bin/node
const fs = require('fs');

const argv = process.argv.slice(2);
if (argv.length === 3) {
  try {
    const data1 = fs.readFileSync(argv[0]);
    const data2 = fs.readFileSync(argv[1]);
    fs.writeFileSync(argv[2], data1);
    fs.appendFileSync(argv[2], data2);
  } catch (e) {
    console.log(e);
  }
} else console.log('Usage: ./102-concat.js <file 1> <file 2> <file 3>');
