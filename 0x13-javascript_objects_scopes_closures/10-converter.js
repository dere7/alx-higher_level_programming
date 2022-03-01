#!/usr/bin/node

exports.converter = function (base) {
  return nums => nums.toString(base);
};
