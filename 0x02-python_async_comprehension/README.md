# 0x02. Python - Async Comprehension

## Resources:books:
Read or watch:
* [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
* [What’s New in Python: Asynchronous Comprehensions / Generators](https://intranet.hbtn.io/rltoken/GeSDerenxLAcZuCZJoCN-Q)
* [Type-hints for generators](https://stackoverflow.com/questions/42531143/type-hinting-generator-in-python-3-6)

---
## Learning Objectives:bulb:
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators

---

### [0. Async Generator](./0-async_generator.py)
* Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module


### [1. Async Comprehensions](./1-async_comprehension.py)
* Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.


### [2. Run time for four parallel comprehensions](./2-measure_runtime.py)
* Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

---

## Author
* **Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
