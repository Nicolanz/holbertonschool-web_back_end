export default function cleanSet(set, startString) {
  let myStr = '';
  if (startString.length === 0) {
    return myStr;
  }

  for (const i of set) {
    if (i.startsWith(startString) && startString !== '') {
      const extr = i.indexOf(startString.slice(-1)) + 1;
      myStr += `${i.substring(extr, i.length)}`;
      myStr += '-';
    }
  }
  return myStr.slice(0, -1);
}
