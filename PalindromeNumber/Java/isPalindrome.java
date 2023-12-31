/* Given an integer x, return true if x is a 
palindrome, and false otherwise. */

class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0) return false;
        int temp = x;
        int rev = 0;
        while(temp != 0){
            rev = rev * 10 + temp % 10;
            temp /= 10;
        }
        return rev == x;
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        System.out.println(obj.isPalindrome(121));
    }
}

