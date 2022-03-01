#!/usr/bin/node

exports.logMe = (function () {
  let i = 0;
  return (item) => console.log(i++ + ':', item);
})();
