# 0x09. Unittests and Integration Tests

## Resources:books:
Read or watch:
* [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
* [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
* [parameterized](https://pypi.org/project/parameterized/)
* [Memoization](https://en.wikipedia.org/wiki/Memoization)

---
## Learning Objectives:bulb:
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* The difference between unit and integration tests.
* Common testing patterns such as mocking, parametrizations and fixtures

---


### [0. Parameterize a unit test](./test_utils.py)
* Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.

### [1. Parameterize a unit test](./test_utils.py)
* Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):
```
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
```
Also make sure that the exception message is as expected.

### [2. Mock HTTP calls](./test_utils.py)
* Define the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result.

### [3. Parameterize and patch](./test_utils.py)
* Read about memoization and familiarize yourself with the `utils.memoize` decorator.

### [4. Parameterize and patch as decorators](./test_client.py)
* In a new `test_client.py` file, declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method.

### [5. Mocking a property](./test_client.py)
* Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`.

### [6. More patching](./test_client.py)
* Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`.

### [7. Parameterize](./test_client.py)
* Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`.

Parametrize the test with the following inputs
```
repo={"license": {"key": "my_license"}}, license_key="my_license"
repo={"license": {"key": "other_license"}}, license_key="my_license"
```
You should also parameterize the expected returned value.

### [8. Integration test: fixtures](./test_client.py)
* We want to test the `GithubOrgClient.public_repos` method in an integration test. That means that we will only mock code that sends external requests.

---

## Author
**Nicolas Zarate** - [Nicolanz](https://github.com/Nicolanz)
