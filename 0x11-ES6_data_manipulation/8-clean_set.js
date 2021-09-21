export default function cleanSet(set, startString) {
  let myStr = '';
  if (!startString || startString.length === 0 || typeof startString !== 'string') {
    return myStr;
  }

  for (const i of set) {
    if (i.startsWith(startString)) {
      myStr += i.slice(startString.length);
      myStr += '-';
    }
  }
  return myStr.slice(0, -1);
}
