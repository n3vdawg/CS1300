#include <iostream>
#include <string>
#include "automata.h"

using namespace std; // yes using namespace std

// NOTE: for directions on what to do with all of these TODOs below,
// please refer to the header file, automata.h.

int prev(int i, int string_size) {
  if (i == 0) {
    return (string_size - 1);
  }
  return (i - 1);
}

int next(int i, int string_size) {
  if (i == (string_size - 1)) {
    return 0;
  }
  return (i + 1);
}

string get_neighborhood(string in, int i) {
  string neighborhood = "";
  char left = in[prev(i, in.length())];
  char mid  = in[i];
  char right = in[next(i, in.length())];
  neighborhood += left;
  neighborhood += mid;
  neighborhood += right;
  return neighborhood;
}

char rule90(string in, int i) {
  if (in[prev(i, in.length())] == '#' && in[next(i, in.length())] == ' ') {
    return '#';
  }
  if (in[prev(i, in.length())] == ' ' && in[next(i, in.length())] == '#') {
    return '#';
  }
  else {
    return ' ';
  }
}

string make_next_generation(string in) {
  string gen = "";
  for (int i = 0; i < in.length(); i++) {
    gen += rule90(in, i);
  }
  return gen;
}


// make automata_main creates a .exe which you can execute with
// ./automata_main

void generate(string initial_state, int num_generations) {
  //set up a cursor variable for whatever next interation is for the loop
  string prior_state = initial_state;
  cout << prior_state << endl;
  for (int i = 0; i < num_generations; i++) {
    prior_state = make_next_generation(prior_state);
    cout << prior_state << endl;
  } 
}

