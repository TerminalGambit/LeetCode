/*
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
*/

/*
Note: The returned array must be malloced, assume caller calls free().
*/

#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *result = malloc(2 * sizeof(int));
    *returnSize = 2;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i+1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
            }
        }
    }
    return result;
}

int main(void) {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;
    int *result = twoSum(nums, 4, target, &returnSize);
    printf("%d %d\n", result[0], result[1]);
    free(result);
    return 0;
}