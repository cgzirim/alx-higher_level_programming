#!/usr/bin/node

function factorial(n)
{
  if(typeof n === 'NaN' || n === 0)
  {
    return(1);
  }
  return(n * factorial(n - 1))
}

let number = parseInt(process.argv[2])
console.log(factorial(number))
