# 0x14. Queuing System in JS

## Resources:books:

* [Redis quick start](https://redis.io/topics/quickstart)
* [Redis client interface](https://redis.io/topics/rediscli)
* [Redis client for Node JS](https://github.com/NodeRedis/node-redis)
* [Kue](https://github.com/Automattic/kue)

---
## Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to run a Redis server on your machine
* How to run simple operations with the Redis client
* How to use a Redis client with Node JS for basic operations
* How to store hash values in Redis
* How to deal with async operations with Redis
* How to use Kue as a queue system
* How to build a basic Express app interacting with a Redis server
* How to the build a basic Express app interacting with a Redis server and queue

---

### [0. Install a redis instance](./dump.rdb)
* Download, extract, and compile the latest stable Redis version

### [1. Node Redis Client](./0-redis_client.js)
* Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

### [2. Node Redis client and basic operations](./1-redis_op.js)
* In a file `1-redis_op.js`, copy the code you previously wrote (0-redis_client.js).

### [3. Node Redis client and async operations](./2-redis_op_async.js)
* In a file `2-redis_op_async.js`, let’s copy the code from the previous exercise (`1-redis_op.js`)

### [4. Node Redis client and advanced operations](./4-redis_advanced_op.js)
* In a file named `4-redis_advanced_op.js`, let’s use the client to store a hash value

### [5. Node Redis client publisher and subscriber](./5-subscriber.js)
* In a file named `5-subscriber.js`, create a redis client

### [6. Create the Job creator](./6-job_creator.js)
* In a file named 6-job_creator.js: create a queue with Kue

### [7. Create the Job processor](./6-job_processor.js)
* In a file named `6-job_processor.js` create a function named sendNotification

### [8. Track progress and errors with Kue: Create the Job creator](./7-job_creator.js)
* In a file named `7-job_creator.js` create an array `jobs` with the following data inside

### [9. Track progress and errors with Kue: Create the Job processor](./7-job_processor.js)
* Create an array that will contain the blacklisted phone numbers. Add in it `4153518780` and `4153518781` - these 2 numbers will be blacklisted by our jobs processor.

### [10. Writing the job creation function](./8-job.js)
* In a file named `8-job.js`, create a function named `createPushNotificationsJobs`

### [11. Writing the test for job creation](./8-job.test.js)
* Now that you created a job creator, let’s add tests. Import the function `createPushNotificationsJobs`

### [12. In stock?](./9-stock.js)
* Create an `express` server listening on the port 1245. (You will start it via: `npm run dev 9-stock.js`)

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
