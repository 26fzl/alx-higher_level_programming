#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let x = 0;
  while ((leng - x) > 0) {
    const aux = list[leng];
    list[leng] = list[x];
    list[x] = aux;
    x++;
    leng--;
  }
  return list;
};
