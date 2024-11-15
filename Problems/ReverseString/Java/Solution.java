package ReverseString.Java;

public class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;  // This should be correct
        char tmp;
        while (left < right) {
            tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        char[] s = {'h', 'e', 'l', 'l', 'o'};
        solution.reverseString(s);
        System.out.println(s);
    }
}
