#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));

if (isNaN(num) === false) {
  for (let i = 0; i < num; i++) {
    let line = '';
    for (let j = 0; j < num; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
