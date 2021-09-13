# 0x0F. ES6 Promises

## Resources:books:

* [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
* [JavaScript Promise: An introduction](https://web.dev/promises/)
* [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
* [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
* [Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

---
## Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* Promises (how, why, and what)
* How to use the then, resolve, catch methods
* How to use every method of the Promise object
* Throw / Try
* The await operator
* How to use an async function

---

### [0. Keep every promise you make and only make promises you can keep](./0-promise.js)
* Return a Promise using this prototype function `getResponseFromAPI()`

### [1. Don't make a promise...if you know you can't keep it](./1-promise.js)
* Using the prototype below, return a `promise`. The parameter is a `boolean`.

### [2. Catch me if you can!](./2-then.js)
* Append three handlers to the function `handleResponseFromAPI(promise)`

### [3. Handle multiple successful promises](./3-all.js)
* In this file, import `uploadPhoto` and `createUser` from `utils.js`
Knowing that the functions in `utils.js` return promises, use the prototype below to collectively resolve all promises and log `body` `firstName` `lastName` to the console.

### [4. Simple promise](./4-user-promise.js)
* Return a resolved promise with this object: `{ firstName: value, lastName: value,}`

### [5. Reject the promises](./5-photo-reject.js)
* Write and export a function named `uploadPhoto`. It should accept one argument `fileName` (string).

### [6. Handle multiple promises](./6-final-user.js)
* Import `signUpUser` from `4-user-promise.js` and `uploadPhoto` from `5-photo-reject.js`.

### [7. Load balancer](./7-load_balancer.js)
* Write and export a function named `loadBalancer`. It should accept two arguments `chinaDownload` (Promise) and `USDownload` (Promise).

### [8. Throw error / try catch](./8-try.js)
* Write a function named `divideFunction` that will accept two arguments: `numerator` (Number) and `denominator` (Number).

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
