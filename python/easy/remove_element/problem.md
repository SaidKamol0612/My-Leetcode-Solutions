# Remove Element

Difficulty: EASY.

[View this problem on Leetcode](https://leetcode.com/problems/remove-element/)

## Description

Given an integer array `num` and an integer `val` in `nums` [in-place](https://en.wikipedia.org/wiki/In-place_algorithm). The order of the elements may be changed. Then return _the number of elements in_ `nums` _which are not equal to_ `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

## Examples

**Input:** nums = [3, 2, 2, 3], val = 3
**Output:** 2, nums = [2, 2, _, _]

**Input:** nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
**Output:** 5, nums = [0, 1, 4, 0, 3, _, _, _]

## Result

![Result-on-Leetcode](result.png)
