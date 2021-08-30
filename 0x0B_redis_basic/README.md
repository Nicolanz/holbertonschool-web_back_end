# 0x0B. Redis basic

## Resources:books:
Read or watch:
* [Redis commands](https://redis.io/commands)
* [Redis python client](https://redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

---
## Learning Objectives:bulb:

* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

---
## Install Redis on Ubuntu 18.04

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

---


### [0. Writing strings to Redis](./exercise.py)
* Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

### [1. Reading from Redis and recovering original type](./exercise.py)
* Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store `"a"` as a UTF-8 string, it will be returned as `b"a"` when retrieved from the server.

### [2. Incrementing values](./exercise.py)
* Familiarize yourself with the `INCR` command and its python equivalent. In this task, we will implement a system to count how many times methods of the `Cache` class are called.

### [3. Storing lists](./exercise.py)
* Familiarize yourself with redis commands `RPUSH`, `LPUSH`, `LRANGE`, etc. In this task, we will define a call_history decorator to store the history of inputs and outputs for a particular function.

### [4. Retrieving lists](./exercise.py)
* In this tasks, we will implement a `replay` function to display the history of calls of a particular function.

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
