#!/usr/bin/node
exports.callMeMoby = function (num, theFunction) {
  for (i = 0; i < num; ++i)
  {
    theFunction()
  }
};