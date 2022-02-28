#!/usr/bin/node

let add = function add(a, b)
{
  console.log(parseInt(a) + parseInt(b))
}

add(process.argv[2], process.argv[3])
