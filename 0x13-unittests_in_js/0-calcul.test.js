
const assert = require('assert');
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', function() {
  it('should return an int number', () => {
      assert.equal(typeof calculateNumber(2.3, 3.1), 'number');
  })
});
