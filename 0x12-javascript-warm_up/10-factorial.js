#!/usr/bin/node
function factorial (number) {
  if (isNaN(number) || number === 1) return 1;
  else return number * factorial(number - 1);
}
const number = parseInt(process.argv[2]);
const result = factorial(number);
console.log(result);
