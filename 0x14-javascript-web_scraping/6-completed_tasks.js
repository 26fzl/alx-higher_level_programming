#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (erro, respo, body) {
  if (erro == null) {
    const respo = {};
    const json = JSON.parse(body);
    for (let x = 0; x < json.length; x++) {
      if (json[x].completed === true) {
        if (respo[json[x].userId] === undefined) {
          respo[json[x].userId] = 0;
        }
        respo[json[x].userId]++;
      }
    }
    console.log(respo);
  }
});
