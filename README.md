Python Performance Benchmark
============================

This repository is Python benchmark for common usage in data science.

Environment: OS Ubuntu 18.04, CPU Intel i5-8400, Python 3.6.5

Pandas I/O
----------

Blog post: 
[Chinese](https://medium.com/@black_swan/pandas-i-o-%E6%95%88%E7%8E%87%E6%B8%AC%E8%A9%A6-c9e20152658a) 
[English](https://medium.com/@black_swan/pandas-i-o-benchmarking-56cd688f832b)

Data: n row x 4 columns random double dataframe.

![Alt text](images/DoubleDataFrame.png)

Remark:
- time or size (Y axis) in log scale.
- Maximum row for excel output is 1048575 rows, so file size and read 
speed of 10^7 are under estimated.
