#!/usr/bin/node
let size;
if ( (size = parseInt(process.argv[2]))) {
  let square = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    if (i + 1 != size)
      square += '\n';
  }
  console.log(square);
}
else console.log('Missing size');
