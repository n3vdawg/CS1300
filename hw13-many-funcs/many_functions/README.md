# The Homework of Many Functions

This homework assignment asks you to implement several functions to
meet a spec. The function specifications will be given in a header
file, along with the function declarations. It is up to you to
implement those functions in a different file.

For example, one function might be to return the sum of the odd
numbers between X and Y, which are integer arguments to the function,
and X is guaranteed to be less than Y. The declaration in the header
file for this hypothetical function could be:

```cpp
// many_functions.h
int sum_odds(int x, int y);
```

The implementation file will initially contain several 'stubs' for
these functions. A stub is simply an empty (or nearly empty)
implementation that has the bare minimum information needed to
compile. The stub for our `sum_odds` function might start out like
this:

```cpp
int sum_odds(int x, int y) {
  return 0;
}
```

Your task is to replace the stubs with function implementations that
meet the spec. An implementation of the `sum_odds` function might be
this:

```cpp
int sum_odds(int x, int y) {
  int sum = 0;
  for (int i=x; i <= y; i++) {
    if ((i % 2) == 1) {
      sum = sum + i;
    }
  }
  return sum;
}
```

When you want to check if your code is correct, compile it and fix any
compiler errors there may be. Once it compiles, run this from the
command line:

```
$ python grade.py many_functions_test
```

It will run some tests on your code and tell you what works and what
doesn't. If something doesn't work, it will tell you the command to
run to see all the details for just that failed test. For example, it
might give you the following command:

```
./many_functions_test "[sum_odds]"
```

Just copy/paste and run that command to get details about the error
messages and line numbers.

## Recap

- function specs are provided in the header file, `many_functions.h`
- stubs will be given in the implementation file, `many_functions.cpp`
- your job is to fill in the stubs according to the specifications
- to test correctness, run the python script just mentioned
- run the command the python script gives to get details

