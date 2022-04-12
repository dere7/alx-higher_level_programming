#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const fs = require('fs');

const url = argv[2];
const fileName = argv[3];
request(url).pipe(fs.createWriteStream(fileName));
