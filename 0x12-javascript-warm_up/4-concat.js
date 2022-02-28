#!/usr/bin/node

let args = process.argv.slice(2);

let fst = typeof args[0] === 'undefined' ? 'undefined' : args[0];
let lst = typeof args[1] === 'undefined' ? 'undefined' : args[1];

console.log(fst + ' is ' + lst)
