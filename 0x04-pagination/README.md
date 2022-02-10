# 0x04. Pagination

-   By Emmanuel Turlay, Staff Software Engineer at Cruise

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/12/3646eb02de6527ca5d83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220210%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220210T175708Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=590ba77c96354540490cb2ff929f06e0fa5bbeffa1e375131feb9542b19a21d4)  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/12/746187b76bea1f46030e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220210%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220210T175708Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=35a196d85e53b95e3fda5195467e1477d8579a31bf5ba93606acc4da5427fc21)  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/12/665ce871c2ecc66a8e71.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220210%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220210T175708Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b5e4ec223d0eece3146fce775ac38fb4391ac19911f4a7a130558270054ec733)


## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/-ZGwuw8X0hQXvV6o5daT_Q "explain to anyone"),  **without the help of Google**:

-   How to paginate a dataset with simple page and page_size parameters
-   How to paginate a dataset with hypermedia metadata
-   How to paginate in a deletion-resilient manner

## Requirements

-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  `python3`  (version 3.7)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/env python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `pycodestyle`  style (version 2.5.*)
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
-   All your functions and coroutines must be type-annotated.