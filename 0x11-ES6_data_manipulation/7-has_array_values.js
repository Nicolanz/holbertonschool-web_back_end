export default function hasValuesFromArray(set, array) {
  for (const i of array) {
    if (set.has(i) === false) {
      return false;
    }
  }
  return true;
}
