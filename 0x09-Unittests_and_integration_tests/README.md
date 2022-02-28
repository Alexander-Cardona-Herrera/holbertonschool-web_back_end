# 0x09. Unittests and Integration Tests

-   By Emmanuel Turlay, Staff Software Engineer at Cruise
-   Weight: 1
-   Ongoing project - started 02-28-2022, must end by 03-03-2022 (in 2 days) - you're done with  0% of tasks.
-   Checker will be released at 03-01-2022 12:00 PM
-   An auto review will be launched at the deadline

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/1/f088970b450e82c881ea.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220228T210818Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=49f19ff5b265752ab9cc9b4c5cc1abd8423f8c0a6eb2f531c9a8f96365324bc6)

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

```
$ python -m unittest path/to/test_file.py

```

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone

-   The difference between unit and integration tests.
-   Common testing patterns such as mocking, parametrizations and fixtures

## Requirements

-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  `python3`  (version 3.7)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/env python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `pycodestyle`  style (version 2.5)
-   All your files must be executable
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
-   All your functions and coroutines must be type-annotated.