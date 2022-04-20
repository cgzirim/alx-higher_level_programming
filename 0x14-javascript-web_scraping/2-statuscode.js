#!/usr/bin/node
/* Displays the status code of a GET request.
- The first argument is the URL to request (GET).
Usage: ./2-statuscode.js <URL> */

const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
