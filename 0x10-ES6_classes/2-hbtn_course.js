export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    } else if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    } else if (Array.isArray(students) === false) {
      throw new TypeError('Students must be an array of strings');
    } else if (students.every((i) => (typeof i === 'string')) !== true) {
      throw new TypeError('Students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (Array.isArray(value) === false) {
      throw new TypeError('Students must be an array of strings');
    } else if (value.every((i) => (typeof i === 'string')) !== true) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
