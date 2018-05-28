# PermMissingElem

Find the missing element in a given permutation.

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5

the function should return 4, as it is the missing element.

Assume that:

- N is an integer within the range [0..100,000];
- the elements of A are all distinct;
- each element of array A is an integer within the range [1..(N + 1)].

Complexity:

- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(1) (not counting the storage required for input arguments).



# Test Results

- Solution 1: https://app.codility.com/demo/results/trainingT9ZXV2-6HT/
- Solution 2: https://app.codility.com/demo/results/training7PP56K-T6R/
- Solution 3: https://app.codility.com/demo/results/trainingF6Q5CB-SQH/
