# 0x0E. ES6 Basics

## Resources:books:

* [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
* [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
* [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
* [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
* [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
* [Javascript ES6 — Iterables and Iterators](https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4?gi=eb7ed81b52f8)
---
## Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

* What ES6 is
* New features introduced in ES6
* The difference between a constant and a variable
* Block-scoped variables
* Arrow functions and function parameters default to them
* Rest and spread function parameters
* String templating in ES6
* Object creation and their properties in ES6
* Iterators and for-of loops

---

### [0. Const or let?](./0-constants.js)
* function taskFirst to instantiate variables using const.

### [1. Block Scope](./1-block-scoped.js)
* Given what you’ve read about var and hoisting, modify the variables inside the function taskBlock so that the variables aren’t overwritten inside the conditional block.

### [2. Arrow functions](./2-arrow.js)
* Rewrite the following standard function to use ES6’s arrow syntax of the function add (it will be an anonymous function after)

### [3. Parameter defaults](./3-default-parameter.js)
* Condense the internals of the following function to 1 line - without changing the name of each function/variable.

### [4. Rest parameter syntax for functions](./4-rest-parameter.js)
* Modify the following function to return the number of arguments passed to it using the rest parameter syntax

### [5. The wonders of spread syntax](./5-spread-operator.js)
* Using spread syntax, concatenate 2 arrays and each character of a string by modifying the function below. Your function body should be one line long.

### [6. Take advantage of template literals](./6-string-interpolation.js)
* Rewrite the return statement to use a template literal so you can the substitute the variables you’ve defined.

### [7. Object property value shorthand syntax](./7-getBudgetObject.js)
* Notice how the keys and the variable names are the same?
Modify the following function’s budget object to simply use the keyname instead.

### [8. No need to create empty objects before adding in properties](./8-getBudgetCurrentYear.js)
* Rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names on the `budget` object

### [9. ES6 method properties](./9-getFullBudget.js)
* Rewrite `getFullBudgetObject` to use ES6 method properties in the `fullBudget` object

### [10. For...of Loops](./10-loops.js)
* Rewrite the function `appendToEachArrayValue` to use ES6’s `for...of` operator. And don’t forget that `var` is not ES6-friendly.

### [11. Iterator](./11-createEmployeesObject.js)
* Write a function named `createEmployeesObject`

### [12. Let's create a report object](./12-log_stats.py)
* Write a function named `createReportObject` whose parameter, `employeesList`, is the return value of the previous function `createEmployeesObject`.

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
