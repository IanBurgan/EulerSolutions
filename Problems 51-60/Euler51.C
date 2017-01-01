#include <stdio.h>

int hasThree(int prime) {
  int digits[10] = { 0 };
  while (prime) {
    digits[prime % 10]++;
    prime /= 10;
  }

  for (size_t i = 0; i < 10; i++) {
    if (digits[i] >= 3) {
      return i;
    }
  }
  return 10;
}

int replace(int num, int old, int now) {
  int altered = 0;
  for (size_t i = 100000; i >= 1; i /= 10) {
    if (num / i % 10 == old) {
      altered += now;
    } else {
      altered += num / i % 10;
    }
    altered *= 10;
  }

  return altered / 10;
}

int main() {
  // first 6 digit prime
  int num = 100003;

  // sieve of primes that are 6 digits long
  int primes[1000000] = { 0 };
  primes[0] = 1;
  primes[1] = 1;
  // eliminate multiples of 2
  for (size_t i = 4; i < 1000000; i += 2) {
    primes[i] = 1;
  }
  // eliminate multiples of primes
  for (size_t i = 1; i < 1000000; i++) {
    if (!primes[i]) {
      for (size_t j = i * i; j < 1000000; j += 2 * i) {
        primes[j] = 1;
      }
    }
  }

  while (num < 1000000) {
    int repeated = hasThree(num);
    // the repeated digit must be 0, 1, or 2
    if (!primes[num] && repeated < 2) {
      int count = 1;
      for (int i = repeated + 1; i < 10; i++) {
        int family = replace(num, repeated, i);
        if (!primes[family]) {
          count++;
        }
      }

      if (count == 8) {
        printf("%d\n", num);
        break;
      }
    }
    num++;
  }

  // number of replacements will be 3
  return 0;
}
