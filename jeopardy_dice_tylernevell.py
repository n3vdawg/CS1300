# Tyler Nevell
#HW 6, Jeopardy Dice


import random

def print_current_player(is_user_turn):
    #Boolean Value Function to determine if it is the human or computers turn
    if is_user_turn == True:
        print("\nIt is now the human's turn.")
    else:
        print("\nIt is now the computer's turn.")
    
def roll_die():
    """Return a dice role 1 - 6"""
    diceThrow = random.randrange(1, 7)     
    return diceThrow
    
def take_turn(is_user_turn, COMPUTER_HOLD, user_turn_total, comp_turn_total):
    #Allow the user to decide whether he wants to continue rolling a dice or not if it is their turn. If it's the computers turn, continue to roll until a one is reached or the computer's score is > 10
    comp_turn_total = 0
    user_turn_total = 0
    #COMPUTER_HOLD = 10
    #while set variable to y, then at end of loop ask if still y
    if is_user_turn == True:
        another_turn = "Y"
        while another_turn == "Y":
            turn = roll_die()
            if turn == 1:
                print("Dice result is", turn)
                user_turn_total = 1
                print("Current turn total =", user_turn_total)
                #another_turn = "N"
                return user_turn_total
            else:
                print("Dice result is", turn)
                user_turn_total = turn + user_turn_total
                print("Current turn total =", user_turn_total)
                another_turn = input("Would you like to roll again? ")
                another_turn = another_turn.upper()
                while another_turn != "Y" and another_turn != "N":
                    print("ERROR")
                    another_turn = input("Would you like to roll again? ")
                    another_turn = another_turn.upper()
                
        return user_turn_total
    
    else:
        while comp_turn_total < COMPUTER_HOLD:
            turn = roll_die()
            
            if turn == 1:
                print("Dice result is ", turn)
                comp_turn_total = 1
                is_user_turn = True
                print("Current turn total =", comp_turn_total)
                return comp_turn_total
                
            else:
                print("Dice result is ", turn)
                comp_turn_total = comp_turn_total + turn
                print("Current turn total =", comp_turn_total)
                
        return comp_turn_total
    

def report_points(user_points_total, computer_points_total):
    #report the total points for the user and computer in the main function
    print("computer user points total:", computer_points_total)
    print("human user points total:", user_points_total, "\n")

def get_next_player(is_user_turn):
    #boolean value to decide whos turn it is
    return not is_user_turn
    
def main():
    print("Welcome to Jeopardy Dice!\n")
    GAME_END_POINTS = 100
    COMPUTER_HOLD = 10
    is_user_turn = True
    computer_points_total = 0
    user_points_total = 0
    report_points(user_points_total, computer_points_total)
    while user_points_total < GAME_END_POINTS and computer_points_total < GAME_END_POINTS:
        print_current_player(is_user_turn)
        #take_turn(is_user_turn, COMPUTER_HOLD, user_points_total, computer_points_total)
        if is_user_turn:
            user_points_total = user_points_total + take_turn(is_user_turn, COMPUTER_HOLD, user_points_total, computer_points_total)
            report_points(user_points_total, computer_points_total)
        else:
            computer_points_total = computer_points_total + take_turn(is_user_turn, COMPUTER_HOLD, user_points_total, computer_points_total)
            report_points(user_points_total, computer_points_total)
        is_user_turn = get_next_player(is_user_turn)
    if user_points_total >= GAME_END_POINTS:
       print("The human user is the winner!!!")
    else:
       print("The computer won! Wahmp-waaaaahhh...")


if __name__ == "__main__":
    main()

