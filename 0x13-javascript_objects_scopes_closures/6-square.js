#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let str = '';
      for (let j = 0; j < this.size; j++) {
        str += c || 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Square;
