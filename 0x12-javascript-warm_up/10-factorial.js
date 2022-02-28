#!/usr/bin/node
function factorial (number) {
  if (isNaN(number) || number === 1) return 1;
  else return number * factorial(number - 1);
}
let number = parseInt(process.argv[2]);
let result = factorial(number);
console.log(result);
