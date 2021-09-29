# 0x13. Unittests in JS

## Resources:books:

* [Mocha documentation](https://mochajs.org/)
* [Chai](https://www.chaijs.com/api/)
* [Sinon](https://sinonjs.org/releases/v7.5.0/)
* [Express](https://expressjs.com/en/guide/routing.html)
* [Request](https://www.npmjs.com/package/request)
* [How to Test NodeJS Apps using Mocha, Chai and SinonJS](https://scotch.io/tutorials/how-to-test-nodejs-apps-using-mocha-chai-and-sinonjs)

---
## Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to use Mocha to write a test suite
* How to use different assertion libraries (Node or Chai)
* How to present long test suites
* When and how to use spies
* When and how to use stubs
* What are hooks and when to use them
* Unit testing with Async functions
* How to write integration tests with a small node server

---

### [0. Basic test with Mocha and Node assertion library](./0-calcul.test.js)
Set up a scripts in your `package.json` to quickly run Mocha using `npm test`

### [1. Combining descriptions](./1-calcul.js)
Create a new file named `1-calcul.js`:

* Upgrade the function you created in the previous task (`0-calcul.js`)
* Add a new argument named `type` at first argument of the function. `type` can be `SUM`, `SUBTRACT`, or `DIVIDE` (string)
* When type is `SUM`, round the two numbers, and add `a` from `b`
* When type is `SUBTRACT`, round the two numbers, and subtract `b` from `a
* When type is `DIVIDE`, round the two numbers, and divide `a` with `b` - if the rounded value of `b` is equal to 0, return the string `Error`

### [2. Basic test using Chai assertion library](./2-calcul_chai.js)
While using Node assert library is completely valid, a lot of developers prefer to have a behavior driven development style. This type being easier to read and therefore to maintain.

### [3. Spies](./3-payment.js)
Spies are a useful wrapper that will execute the wrapped function, and log useful information (e.g. was it called, with what arguments). Sinon is a library allowing you to create spies.


### [4. Stubs](./4-payment.js)
Stubs are similar to spies. Except that you can provide a different implementation of the function you are wrapping. Sinon can be used as well for stubs.

### [5. Hooks](./5-payment.js)
Hooks are useful functions that can be called before execute one or all tests in a suite

### [6. Async tests with done](./6-payment_token.test.js)
Look into how to support async testing, for example when waiting for the answer of an API or from a Promise

### [7. Skip](./7-skip.test.js)
When you have a long list of tests, and you can’t figure out why a test is breaking, avoid commenting out a test, or removing it. Skip it instead, and file a ticket to come back to it as soon as possible

### [8. Basic Integration testing](./8-api/api.js)
In a folder `8-api` located at the root of the project directory, copy this `package.json` over.

### [9. Regex integration testing](./9-api/api.test.js)
In a folder `9-api`, reusing the previous project in `8-api` (`package.json`, `api.js` and `api.test.js`)

### [10. Deep equality & Post integration testing](./10-api/api.test.js,)
In a folder `10-api`, reusing the previous project in `9-api` (`package.json`, `api.js` and `api.test.js`)

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
