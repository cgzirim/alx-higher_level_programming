#!/usr/bin/node

size = process.argv[2]
if(isNaN(size))
{
  console.log('Missing size')
}
else
{
  s = ""
  for(let i = 0; i < size; i++)
  {
    for(let j = 0; j < size; j++)
    {
      s += 'X';
    }
    if(i < size - 1)
    {
      s += '\n'
    }
  }

  console.log(s)
}
