#!/usr/bin/node
const dict = require('./101-data.js').dict

let output = {}
let list = []
let len = 6;
while (len > 0) {
    for (const [key, value] of Object.entries(dict)) {
        let currentValue = value;
        if (value === currentValue) {
            if (Array.isArray(output.value)) continue;
            else { output[value] = [];}
            output[value].push(key)
            delete dict.value
        }
    }
    len -= 1;
}

console.log(output)
console.log(dict)
