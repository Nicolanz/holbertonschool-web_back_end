# 0x04. Pagination

## Resources:books:
Read or watch:
* [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
* [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

---
## Learning Objectives:bulb:
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to paginate a dataset with simple page and page_size parameters
* How to paginate a dataset with hypermedia metadata
* How to paginate in a deletion-resilient manner

---

### [0. Simple helper function](./0-simple_helper_function.py)
* Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

### [1. Simple pagination](./1-simple_pagination.py)
* Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.


### [2. Hypermedia pagination](./2-hypermedia_pagination.py)
* Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary.

### [3. Deletion-resilient hypermedia pagination](./3-hypermedia_del_pagination.py)
* The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.


---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
