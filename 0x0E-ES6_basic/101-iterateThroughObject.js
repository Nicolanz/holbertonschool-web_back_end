export default function iterateThroughObject(reportWithIterator) {
  let returnString = '';
  for (const idx of reportWithIterator) {
    returnString += `${idx} | `;
  }
  return returnString;
}
