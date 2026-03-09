# File Analysis with Iterators in Python

> **Project:** Text Stream Processing and Operating System Error Handling

> **Author:** Diego Padilla

> **Technologies:** Python 3, WSL (Linux), GitHub


## Python File Processing

The program developed in this exercise demonstrates the efficient use of the `strerror` method.

During development, an `import` statement is used to access the `strerror` function of my operating system. 
This code uses a `try` block with all the content inside. It has two counters, `count` and `line_count`, which 
are initially set to 0.

* **Inside, a `for` loop opens the file using `open('filename', 'rt')`.

* **Then, it increments `line_count` by 1.

* **Next, a nested `for` loop increments `count` by 1. This `for` loop prints the text saved in the `.txt` file.

* **Once the `for` loops finish, a message is printed indicating the number of characters or letters 
  in the `.txt` file using the `count` counter.

* **Finally, it prints the number of lines using the `line_count` counter.
 
* **Finally, the `except uses IOError as e:` indicating that there was an error trying to open the file using 
  `strerror(e.errno)` indicating that it did not find the directory. 



