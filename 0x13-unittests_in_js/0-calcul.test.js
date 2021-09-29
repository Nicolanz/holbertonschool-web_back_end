
const assert = require('assert');
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', function() {
  it('should return an int number', () => {
      assert.equal(typeof calculateNumber(2.3, 3.1), 'number', 'result is not rounded');
  });
  it('should return sum of nums', () => {
      assert.equal(calculateNumber(2.2, 2,3), 4, "Not expected result");
  });
  it('should return sum of nums', () => {
      assert.equal(calculateNumber(1, 3), 4, "Not expected result");
  });
  it('should return sum of nums', () => {
      assert.equal(calculateNumber(1, 3.7), 5, "Not expected result");
  });
  it('should return sum of nums', () => {
      assert.equal(calculateNumber(1.2, 3.7), 5, "Not expected result");
  });
  it('should return sum of nums', () => {
      assert.equal(calculateNumber(1.5, 3.7), 6, "Not expected result");
  });
});
