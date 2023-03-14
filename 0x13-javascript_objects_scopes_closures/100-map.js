#!/usr/bin/node
const array = require('./100-data').list;

const newArray = array.map((key,val) => val * key)
console.log(array);
console.log(newArray);