#!/usr/bin/node
let agrc = process.argv.length;

if (agrc == 3) {
  console.log("Argument found");
} else if (agrc > 3) {
  console.log("Arguments found");
} else {
  console.log("No argument");
}
