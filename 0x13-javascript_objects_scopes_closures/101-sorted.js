#!/usr/bin/node

/**
 * The script that imports a dictionary of occurrences
 * It import dict from the file 101-data.js
 */
const initDict = require('./101-data').dict;
const newDict = {};

for (const key in initDict) {
  if (newDict[initDict[key]] === undefined) {
    newDict[initDict[key]] = [];
  }
  newDict[initDict[key]].push(key);
}

console.log(newDict);
