#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));

if (isNaN(num) === false) {
  for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
} else {
  console.log('Missing number of occurrences');
}
