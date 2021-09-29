const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return an int number', () => {
    assert.equal(typeof calculateNumber(2.3, 3.1), 'number');
  });
  it('should return sum of num', () => {
    assert.equal(calculateNumber(2.2, 2, 3), 4);
  });
  it('should return sum', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it('sum of nums', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('return sum of nums', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('sum', () => {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
});
