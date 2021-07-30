# 0x05. Personal data

## Resources:books:
Read or watch:
* [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
* [logging documentation](https://docs.python.org/3/library/logging.html)
* [bcrypt package](https://github.com/pyca/bcrypt/)
* [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

---
## Learning Objectives:bulb:
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* Examples of Personally Identifiable Information (PII)
* How to implement a log filter that will obfuscate PII fields
* How to encrypt a password and check the validity of an input password
* How to authenticate to a database using environment variables

---

### [0. Regex-ing](./filtered_logger.py)
* Write a function called `filter_datum` that returns the log message obfuscated.

### [1. Log formatter](./filtered_logger.py)
* Update the class to accept a list of strings fields constructor argument.

### [2. Create logger](./filtered_logger.py)
* Implement a `get_logger` function that takes no arguments and returns a `logging.Logger` object.

### [3. Connect to secure database](./filtered_logger.py)
* Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.

### [4. Read and filter data](./filtered_logger.py)
* Implement a `main` function that takes no arguments and returns nothing.

### [5. Encrypting passwords](./encrypt_password.py)
* Implement a `hash_password` function that expects one string argument name password and returns a salted, hashed password, which is a byte string.

### [6. Check valid password](./encrypt_password.py)
* Implement an `is_valid` function that expects 2 arguments and returns a boolean.

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
