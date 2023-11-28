#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (erro, data) => {
  if (erro) {
    console.error(erro);
  } else {
    console.log(data);
  }
});
