import numpy as np
from time import time


def matrix_mul(size, n=100):
    # reference: https://markus-beuckelmann.de/blog/boosting-numpy-blas.html
    np.random.seed(112)
    a, b = np.random.random((size, size)), np.random.random((size, size))
    t = time()
    for _ in range(n):
        np.dot(a, b)
    delta = time() - t
    print('Dotted two matrices of size %dx%d in %0.4f ms.' % (size, size, delta / n * 1000))


def vector_mul(size, n=100):
    # reference: https://markus-beuckelmann.de/blog/boosting-numpy-blas.html
    np.random.seed(112)
    a, b = np.random.random((size, size)), np.random.random((size, size))
    t = time()
    for _ in range(n):
        np.dot(a, b)
    delta = time() - t
    print('Dotted two vector of length %d in %0.4f ms.' % (size, delta / n * 1000))


def svd_decomposition(size, n=10):
    np.random.seed(112)
    a = np.random.random((size, size))
    t = time()
    for _ in range(n):
        np.linalg.svd(a, full_matrices=False)
    delta = time() - t
    print('SVD decomposition of size %dx%d in %0.4f ms.' % (size, size, delta / n * 1000))


def eigen_decomposition(size, n=10):
    np.random.seed(112)
    a = np.random.random((size, size))
    t = time()
    for _ in range(n):
        np.linalg.eig(a)
    delta = time() - t
    print('Eigen decomposition of size %dx%d in %0.4f ms.' % (size, size, delta / n * 1000))


def main():
    print('Numpy config')
    print(np.__config__.show())
    vector_mul(size=8192, n=50)
    matrix_mul(size=8192, n=50)
    svd_decomposition(2048, n=50)
    eigen_decomposition(2048, n=50)


if __name__ == '__main__':
    main()
