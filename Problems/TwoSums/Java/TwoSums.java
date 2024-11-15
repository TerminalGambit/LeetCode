/*
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
*/

class twoSums {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        int i = 0;
        int j = 0;
        boolean found = false;
        while (i < nums.length && !found) {
            j = i + 1;
            while (j < nums.length && !found) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    found = true;
                }
                j++;
            }
            i++;
        }
        return result;
    }

    public static void main(String[] args) {
        twoSums ts = new twoSums();
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        int[] result = ts.twoSum(nums, target);
        System.out.println(result[0] + " " + result[1]);
    }
}