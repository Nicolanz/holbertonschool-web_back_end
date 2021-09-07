# 0x0C. MySQL advanced

## Resources:books:

* [Read or watch:](https://riak.com/resources/nosql-databases/)
* [NoSQL Databases Explained](https://www.youtube.com/watch?v=qUV2j3XBRHc)
* [What is NoSQL ?](https://www.youtube.com/watch?v=ClAQEARNUoQ)
* [Building Your First Application: An Introduction to MongoDB](https://www.youtube.com/watch?v=ClAQEARNUoQ)
* [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
* [Aggregation](https://docs.mongodb.com/manual/aggregation/)
* [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
* [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/)
* [The mongo Shell](https://docs.mongodb.com/manual/reference/mongo/)

---
## Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

* What NoSQL means
* What is difference between SQL and NoSQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB

---

### [0. List all databases](./0-list_databases)
* Write a script that lists all databases in MongoDB.

### [1. Create a database](./1-use_or_create_database)
* Write a script that creates or uses the database `my_db`

### [2. Insert document](./2-insert)
Write a script that inserts a document in the collection `school`

### [3. All documents](./3-all)
* Write a script that lists all documents in the collection `school`

### [4. All matches](./4-match)
* Write a script that lists all documents with name="Holberton school" in the collection `school`

### [5. Count](./5-count)
* Write a script that displays the number of documents in the collection `school`

### [6. Update](./6-update)
* Write a script that adds a new attribute to a document in the collection `school`

### [7. Delete by match](./7-delete)
* Write a script that deletes all documents with `name="Holberton school"` in the collection `school`

### [8. List all documents in Python](./8-all.py)
* Write a Python function that lists all documents in a collection

### [9. Insert a document in Python](./9-insert_school.py)
* Write a Python function that inserts a new document in a collection based on `kwargs`

### [10. Change school topics](./10-update_topics.py)
* Write a Python function that changes all topics of a school document based on the name

### [11. Where can I learn Python?](./11-schools_by_topic.py)
* Write a Python function that returns the list of school having a specific topic.

### [12. Log stats](./12-log_stats.py)
* Write a Python script that provides some stats about Nginx logs stored in MongoDB

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
