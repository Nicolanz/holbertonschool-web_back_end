# 0x10. ES6 classes

## Resources:books:

* [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [Metaprogramming](https://www.keithcirkel.co.uk/metaprogramming-in-es6-symbols/#symbolspecies)

---
## Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to define a Class
* How to add methods to a class
* Why and how to add a static method to a class
* How to extend a class from another
* Metaprogramming and symbols

---

### [0. You used to attend a place like this at some point](./0-classroom.js)
* Implement a class named `ClassRoom`.

### [1. Let's make some classrooms](./1-make_classrooms.js)
* Import the `ClassRoom` class from `0-classroom.js`. Implement a function named `initializeRooms`. It should return an array of 3 `ClassRoom` objects with the sizes 19, 20, and 34 (in this order).

### [2. A Course, Getters, and Setters](./2-hbtn_course.js)
* Implement a class named `HolbertonCourse`.

### [3. Methods, static methods, computed methods names..... MONEY](./3-currency.js)
* Implement a class named `Currency`.

### [4. Pricing](./4-pricing.js)
* Import the class Currency from `3-currency.js` Implement a class named `Pricing`.

### [5. A Building](./5-building.js)
* Implement a class named `Building`.

### [6. Inheritance](./6-sky_high.js)
* Import Building from `5-building.js`. Implement a class named `SkyHighBuilding` that extends from `Building`.

### [7. Airport](./7-airport.js)
* Implement a class named `Airport`.

### [8. Primitive - Holberton Class](./8-hbtn_class.js)
* Implement a class named `HolbertonClass`.

### [9. Hoisting](./9-hoisting.js)
* Fix this code and make it work.
```
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  get fullStudentDescription() {
    return `${self._firstName} ${self._lastName} - ${self._holbertonClass.year} - ${self._holbertonClass.location}`;
  }
}


export const listOfStudents = [student1, student2, student3, student4, student5];
```

### [10. Vroom](./10-car.js)
* Implement a class named Car.

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
