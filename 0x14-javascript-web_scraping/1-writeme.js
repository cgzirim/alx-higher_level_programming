#!/usr/bin/node
/* Writes a string to a file.
- The first argument is the file path.
- The second argument is the string to write.
Usage: ./1-writeme.js <file path> <string to write>
*/

const fs = require('fs');
const content = process.argv[3];

fs.writeFile(process.argv[2], content, err => {
  if (err) {
    console.error(err);
  }
});
