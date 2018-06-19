#include "many_functions.h"

// NOTE: see many_functions.h for documentation for all of the
// functions, and for these TODOs below.

int echo(int n) {
  return n;
}

int add_four(int n) {
  int x = n + 4;
  return x;
}

int count_odds(int a, int b) {
  int count = 0;
  for (int i = a; i <= b; i++) {
    if ((i % 2) != 0) {
      count = count + 1; 
    }
  }
  return count;
}

bool is_prime(int n) {
  for (int i = 2; i < n; i++) {
    if ((n % i) == 0) {
      return false;
    }
  }
  return true; 
}

float quadratic(float a, float b, float c, float x) {
  float quad = (a * (x*x)) + (b * x) + c;  
  return quad;
}

bool ftol(float a, float b, float tol) {
  float upper = b + tol;
  float lower = b - tol;
  if (a < upper && a > lower) {
    return true;
  }
  return false;
}

bool is_bleep(int n) {
  if (((n % 3) == 0 || (n % 7) == 0) || (n > 10 && n < 20)) {
    return true;
  }
  return false;
}

bool is_blop(int n) {
  if (((n % 4) == 0) || (n > 35 && (n % 5) == 0)) {
    return true;
  }
  return false;
}

bool is_bleebleblam(int n) {
  if (is_blop(n) && is_bleep(n)) {
    return true;
  }
  return false;
}
