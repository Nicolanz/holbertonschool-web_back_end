const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        const newArray = { data };
        resolve(newArray);
      }
    });
  });
}

module.exports = readDatabase;
