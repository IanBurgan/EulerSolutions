#include <stdio.h>

int sameDigits(int a, int b) {
  int aDigits[10] = { 0 };
  int bDigits[10] = { 0 };
  int min;

  if (b < a) {
    int temp = a;
    a = b;
    b = temp;
  }

  while (a) {
    aDigits[a % 10] += 1;
    bDigits[b % 10] += 1;

    a /= 10;
    b /= 10;
  }

  if (b > 0) {
    return 0;
  }

  for (size_t i = 0; i < 10; i++) {
    if (aDigits[i] != bDigits[i]) {
      return 0;
    }
  }

  return 1;
}

int main() {
  for (int i = 100000; i < 1000000 / 6; i++) {
    if (sameDigits(i, 2 * i) && sameDigits(i, 3 * i) && sameDigits(i, 4 * i)) {
      if (sameDigits(i, 5 * i) && sameDigits(i, 6 * i)) {
        printf("%d\n", i);  
      }
    }
  }

  return 0;
}
