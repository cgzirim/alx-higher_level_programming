#!/usr/bin/node

const args = process.argv.slice(2);

const fst = typeof args[0] === 'undefined' ? 'undefined' : args[0];
const lst = typeof args[1] === 'undefined' ? 'undefined' : args[1];

console.log(fst + ' is ' + lst);
