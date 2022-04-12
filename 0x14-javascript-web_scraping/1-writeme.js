#!/usr/bin/node
const { writeFile } = require('fs');
const { argv } = require('process');

writeFile(argv[2], argv[3], 'utf8', function (err) {
  if (err) console.log(err);
});
