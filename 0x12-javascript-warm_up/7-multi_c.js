#!/usr/bin/node

arg = process.argv[2]
if (isNaN(arg))
{
  console.log('Missing number of occurrences');
}

for(let i = 0; i < arg; i++)
{
  console.log("C is fun");
}
