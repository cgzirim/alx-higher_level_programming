#!/usr/bin/node
module.exports = class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) { [this.width, this.height] = [w, h];}        
    }

    print() {
        for (let r = 0; r < this.height; r++) {
            let row = '';
            for(let c = 0; c < this.width; c++) row += 'X';
            console.log(row);
        }
    }
};