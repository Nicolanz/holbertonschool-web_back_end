const fs = require('fs');

function countStudents() {
  try {
    let data = fs.readFileSync('./database.csv', { encoding: 'utf8', flag: 'r' });
    let counter = 0;
    const newObj = {};

    data = data.split('\n');

    for (const i in data) {
      data[i] = data[i].split(',');
    }

    for (let i = 1; i < data.length; i += 1) {
      if (data[i].length > 1) {
        counter += 1;
        if (!newObj.hasOwnProperty(data[i][data[i].length - 1])) {
          newObj[data[i][data[i].length - 1]] = {
            count: 1,
            names: [data[i][0]],
          };
        } else {
          newObj[data[i][data[i].length - 1]].count += 1;
          newObj[data[i][data[i].length - 1]].names.push(data[i][0]);
        }
      }
    }
    console.log(`Number of students: ${counter}`);

    for (const property in newObj) {
      console.log(`Number of students in ${property}: ${newObj[property].count}. List: ${newObj[property].names.join(', ')}`);
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
