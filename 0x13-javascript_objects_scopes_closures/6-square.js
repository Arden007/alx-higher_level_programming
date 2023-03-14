#!/usr/bin/node
const firstSquare = require("./5-square");

class Square extends firstSquare {
  charPrint(c) {
    if (c === undefined) 
    {
        for (var i = 0; i < this.height; i++) {
          let sqr = "";
          for (var j = 0; j < this.width; j++) {
            sqr += "X";
          }
          console.log(sqr);
        }
    }
    else 
    {
        for (var i = 0; i < this.height; i++) {
          let sqr = "";
          for (var j = 0; j < this.width; j++) {
            sqr += c;
          }
          console.log(sqr);
        }
    }
  }
}

module.exports = Square;