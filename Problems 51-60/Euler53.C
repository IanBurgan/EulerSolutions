#include <stdio.h>

long long combo(int n, int r) {
  if (r > n / 2) {
    r = n - r;
  }
  if (r == 0) {
    return 1;
  } else {
    int num = combo(n, r - 1);
    // stop calculating if already > 1000000
    if (num > 1000000) {
      return num;
    } else {
      return num * (n - r + 1) / r;
    }
  }
}

int main() {
  int count = 0;
  for (int i = 1; i < 101; i++) {
    for (int j = 0; j < i; j++) {
      if (combo(i, j) > 1000000) {
        count++;
      }
    }
  }
  printf("%d\n", count);
  return 0;
}
