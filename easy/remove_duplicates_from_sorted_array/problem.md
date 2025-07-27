# Remove Duplicates from Sorted Array

Difficulty: EASY.

[View this problem on Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Description

Given an integer array `num` sorted in **non-decreasing order**, remove the dupliate [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the element should be kept the **same**. Then return _the number of unique elements in_ `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

## Examples

**Input:** nums = [1, 1, 2]
**Output:** 2, nums = [1, 2, _]

**Input:** nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
**Output:** 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

## Result

![Result-on-Leetcode](result.png)
