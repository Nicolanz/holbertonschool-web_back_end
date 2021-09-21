export default function cleanSet(set, startString) {
  let myStr = '';
  for (const i of set) {
    if (i.startsWith(startString) && startString !== '') {
      const extr = i.indexOf(startString.slice(-1)) + 1;
      myStr = `${myStr}-${i.substring(extr, i.length)}`;
    }
  }
  myStr = myStr.substring(1);
  return myStr;
}
