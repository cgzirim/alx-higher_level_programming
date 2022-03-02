#!/usr/bin/node
exports.esrever = function (list) {
  // Returns the reversed version of a list.
  const output = [];
  while (list.length) {
    output.push(list.pop());
  }
  return output;
};
