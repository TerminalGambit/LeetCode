#include <stdio.h>

void reverseString(char* s, int sSize) {
    int left = 0;
    int right = sSize - 1;
    int tmp;
    while (left < right) {
        tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
        left++;
        right--;
    }
}

int main(void) {
    char s[] = "hello";
    reverseString(s, 5);
    printf("%s\n", s);
    return 0;
}