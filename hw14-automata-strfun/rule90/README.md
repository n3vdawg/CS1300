# Cellular Automata

In this assignment you'll make a full program built that implements
the "Rule 90" cellular automata. (Read about it on Wikipedia!)

The basic idea is that you have a string that represents a generation:

```
-||-|---|-||--|-||
```

One character means on, the other means off. In this homework, we're
going to use `#` to represent on, and ` ` (space character) for
off. This makes the output a bit more interesting because there's a
lot of contrast. You could use dashes and pipes like I did above.

Anyway, based on an initial generation and a set of rules, we can
build later generations that can form interesting patterns. For our
purposes, we're displaying each generation as a new line directly
below the earlier one.

**In Rule 90, a cell in the next generation is on if and only if exactly
one of the cell's neighbors from the previous generation is on.**

So to calculate (say) the next value of cell 8, we have to look at the
current value of cells 7, 8, and 9. Actually, the current value of
cell 8 isn't needed, but those three (cells 7, 8, 9) form the
"neighborhood" of interest. 

The tricky thing is that we will treat the generation strings as
circular. That means the element to the left of cell zero is the last
cell; the element to the right of the last cell is at index zero.

## What To Implement

You'll fill in all of the TODOs in the `automata.cpp` file. But the
instructions for each function are in the header file, `automata.h`.

## Running Tests

Build the tests with `make` (it is the default target) and run the
tests either using the python script (`python grade.py automata_test`)
or directly with `./automata_test`.

## Running The Cellular Automata Program

This is optional but you might find it fun. Build the cellular
automata program with `make automata_main`, and run it with
`./automata_main`. If your implementation works, you should get output
that looks like that in the `example_output.txt` file.

## Advice

It is recommended that you implement functions in the order they
appear in the `points.json` file. This is for your mental health; by
implementing the easier functions first, you will get into the swing
of things. And, later functions will depend on the earlier ones. So if
your `prev` and `next` functions both work, it will be a lot easier to
implement the `get_neighborhood` function.
