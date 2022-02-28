#!/usr/bin/node

const nums = process.argv.slice(2);
let max = 0;
if (nums.length < 2) {
  console.log(0);
} else {
  max = 0;
  for (let i = 0; i < nums.length; i++) {
    if (parseInt(nums[i]) > max) {
      max = parseInt(nums[i]);
    }
  }

  console.log(max);
}
