# 0x11. ES6 data manipulation

## Resources:books:

* [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
* [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
* [Set Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
* [Map Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
* [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

---
## Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to use map, filter and reduce on arrays
* Typed arrays
* The Set, Map, and Weak link data structures


---

### [0. Basic list of objects](./0-get_list_students.js)
* Create a function named `getListStudents` that returns an array of objects.

### [1. More mapping](./1-get_list_student_ids.js)
* Create a function `getListStudentIds` that returns an array of ids from a list of object.

### [2. Filter](./2-get_students_by_loc.js)
* Create a function `getStudentsByLocation` that returns an array of objects who are located in a specific city.

### [3. Reduce](./3-get_ids_sum.js)
* Create a function `getStudentIdsSum` that returns the sum of all the student ids.

### [4. Combine](./4-update_grade_by_city.js)
* Create a function `updateStudentGradeByCity` that returns an array of students for a specific city with their new grade

### [5. Typed Arrays](./5-typed_arrays.js)
* Create a function named `createInt8TypedArray` that returns a new `ArrayBuffer` with an `Int8` value at a specific position.

### [6. Set data structure](./6-set.js)
* Create a function named `setFromArray` that returns a `Set` from an array.

### [7. More set data structure](./7-has_array_values.js)
* Create a function named `hasValuesFromArray` that returns a boolean if all the elements in the array exist within the set.

### [8. Clean set](./8-clean_set.js)
* Create a function named `cleanSet` that returns a string of all the set values that start with a specific string (`startString`).

### [9. Map data structure](./9-groceries_list.js)
* Create a function named `groceriesList` that returns a map of groceries with the following items (name, quantity):
```
Apples, 10
Tomatoes, 10
Pasta, 1
Rice, 1
Banana, 5
```

### [10. More map data structure](./10-update_uniq_items.js)
* Create a function named `updateUniqueItems` that returns an updated map for all items with initial quantity at 1.

### [11. Weak link data structure](./100-weak.js)
* Export a const instance of WeakMap and name it weakMap. Export a new function named queryAPI. It should accept an endpoint argument like so:
```
  {
    protocol: 'http',
    name: 'getUsers',
  }
```

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
