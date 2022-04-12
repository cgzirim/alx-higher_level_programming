#!/usr/bin/node
/* Reads and prints the content of a file.
- The first argument is the file path.
Usage: ./0-readme.js <file path> */


const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
