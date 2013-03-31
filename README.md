checkFibonacci
==============

check if a number is a Fibonacci and compare speed of two methods

Two methods were proposed in quora 

http://www.quora.com/Algorithms/What-is-the-most-efficient-algorithm-to-check-if-a-number-is-a-Fibonacci-Number

where Anders claimed his matrix speed is couple of times faster than John's perfect square method, while John claimed
some optimizations were needed since he used a slow is_square method.

To compare both of these nice algorithms, I implemented Anders' code in python, as well as John's, plus the fastest
Newton's method to determine if a number is a perfect square number.

==== the test and result

the test is using a list of first 500 Fibonacci from this website: http://planetmath.org/listoffibonaccinumbers
the method is running over this list for 100 times for each algorithm.
the machine is a Macbook Pro with Mac OS X 10.7.

The python releases are:

Python: Python 2.7.1 (r271:86832, Jul 31 2011, 19:30:53)

PyPy: PyPy 1.9.0 with GCC 4.2.1

The result is very intersting: it depends on python optimization.

If use python 2.7:

% python is_fib.py
Anders method: 1.52931690216
John method: 1.36000704765

% pypy is_fib.py
Anders method: 0.799499988556
John method: 2.0126721859

Matrix mutiplication recursion is highly optimized in pypy, but John's method is 10% faster in the official python 2.7.

