export default function cleanSet(set, startString) {
  if (startString.length === 0 || typeof startString !== 'string'
    || typeof set !== 'object'
  ) {
    return '';
  }
  const myStr = [];
  for (const i of set) {
    if (i.startsWith(startString)) {
      myStr.push(i.slice(startString.length));
    }
  }
  return myStr.join('-');
}
