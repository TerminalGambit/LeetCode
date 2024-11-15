/* Given an signed integer x, return true if x is a 
palindrome, and false otherwise.
*/
#include <stdio.h>

int isPalindrome(int x) {
    if (x < 0) return 0;
    long rev = 0, temp = x;
    while (temp) {
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    return rev == x;
}

int main(void) {
    int x = -121;
    printf("%d\n", isPalindrome(x));
    return 0;
}