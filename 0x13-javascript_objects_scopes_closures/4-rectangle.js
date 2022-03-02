#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    // Prints the rectangle using the character X
    for (let r = 0; r < this.height; r++) {
      let row = '';
      for (let c = 0; c < this.width; c++) row += 'X';
      console.log(row);
    }
  }

  rotate () {
    // Exchanges the width and the height of the rectangle.
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    // Multiples the width and the height of the rectangle by 2.
    this.width *= 2;
    this.height *= 2;
  }
};
