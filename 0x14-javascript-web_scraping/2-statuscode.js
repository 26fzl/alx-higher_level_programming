#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (erro, respo) => {i
  if (erro) {
    console.error(erro);
  } else {
    console.log(`code: ${respo.statusCode}`);
  }
});
