#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    // Prints the rectangle using the character c.
    if (typeof char === 'undefined') this.print();
    else {
      for (let r = 0; r < this.height; r++) {
        let row = '';
        for (let c = 0; c < this.width; c++) row += char;
        console.log(row);
      }
    }
  }
};
