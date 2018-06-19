//
// jeopardy.cpp
//

#include "jeopardy.h"
#include <string>
#include <cstdlib>
#include <ctime>
#include <iostream>

 

bool initialize_randomness() {
  srand(time(NULL));
  return true;
}

void print_current_player(bool is_user_turn) {
  using namespace std;
  if (is_user_turn == true) {
    cout << "It is now human's turn" << endl;
  }
  if (is_user_turn == false) {
    cout << "It is now computer's turn" << endl;
  }
}

int roll_die() {
  int roll = (rand() % 6) + 1;
  return roll;
}

int take_turn(bool is_user_turn, int computer_hold_threshold) {
  using namespace std;
  int user_rolltot = 0;
  int comp_rolltot = 0;
  if (is_user_turn == true) {
    string another_turn = "y";
    while (another_turn == "y") {
      int turn = roll_die();
      if (turn == 1) {
        string roll = "roll: " + to_string(turn);
        cout << roll << endl;
        user_rolltot = 1;
        cout << "bummer! you rolled a 1." << endl;
        return user_rolltot;
      }
      else {
        string roll = "roll: " + to_string(turn);
        cout << roll << endl;
        user_rolltot = user_rolltot + turn;
        string stri_tots = "total so far: " + to_string(user_rolltot);
        cout << stri_tots << endl;
        cout << "roll again?: [yn]" << endl;
        string another_turn;
        cin >> another_turn;
      }
    }
    return user_rolltot; 
  }
  else {
    while (comp_rolltot < computer_hold_threshold) {
      int turn = roll_die();
      if (turn == 1) {
        comp_rolltot = 1;
        cout << "roll: 1" << endl;
        is_user_turn = true;
        return comp_rolltot;
      }
      else {
        comp_rolltot = comp_rolltot + turn;
        string roll = "roll: " + to_string(turn);
        cout << roll << endl;
      }
    }
    string computer_hold = "*computer holds at " + to_string(comp_rolltot) + "*";
    cout << computer_hold << endl;
    return comp_rolltot;
  }
}    

void report_points(int human_total, int computer_total) {
  using namespace std;
  string hum_tot = "human:    " + to_string(human_total);
  string com_tot = "computer: " + to_string(computer_total);
  cout << hum_tot << endl;
  cout << com_tot << endl;
}

bool get_next_player(bool is_user_turn) {
  return not is_user_turn;
}

void play_game() {
  using namespace std;
  int GAME_END_POINTS = 100;
  int computer_hold_threshold = 10;
  bool is_user_turn = true;
  int computer_total = 0;
  int human_total = 0;
  report_points(human_total, computer_total);
  while (human_total < GAME_END_POINTS && computer_total < GAME_END_POINTS) {
    print_current_player(is_user_turn);
    if (is_user_turn == true) {
      human_total = human_total + take_turn(is_user_turn, computer_hold_threshold);
      report_points(human_total, computer_total);
    }
    else {
      computer_total = computer_total + take_turn(is_user_turn, computer_hold_threshold);
      report_points(human_total, computer_total);
    }
    is_user_turn = get_next_player(is_user_turn);
  }
  if (human_total >= GAME_END_POINTS) {
    cout << "The human user is the Winner!" << endl;
  }
  else {
    cout << "The computer won! Wahmp-waaaaaahhhh..." << endl;
  }
}
