export default function createInt8TypedArray(length, position, value) {
  const int32View = new Int8Array(length);
  try {
    int32View[position] = value;
  } catch (e) {
    throw new Error('Position outside range');
  }
  return new DataView(int32View.buffer);
}
