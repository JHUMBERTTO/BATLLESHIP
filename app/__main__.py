from functions import fill_board as fb, create_board as cb, cool_board as ccb, ships_left as sl, shoot_position as sp
from random import randint
from math import sqrt
import time

 
def main():
    while True:
        try:
            print("Welcome to Battleship game! - First you need to create your board\n")

            # ---config of the game---

            # input size
            size = int(input("Specify the size of your matrix: "))

            #create the boards
            matrix_p1 = cb.create_board(size)
            ccb.cool_board(matrix_p1)

            # init computer board with the same size
            computer_board = cb.create_board(size)

            # fill the board 
            number_of_ships = round(size+sqrt(size))

            filled = fb.fill_board(matrix_p1, number_of_ships)

            # fill computer board
            filled_computer = fb.fill_computer_board(computer_board, number_of_ships)
            # ccb.cool_board(filled_computer)

            #--- game on ---
            print("\n" * 50)  # Clear screen
            print("Let the game begin!\n")
            
            turn = 1
            while True:
                if turn == 1:
                    time.sleep(1)
                    print("🌊 Computer's Turn ... 🌊")
                    time.sleep(1)
                    computer_shoot = [randint(0, size - 1),randint(0, size - 1)]

                    print(f"The computer shot at: {computer_shoot}")
                    time.sleep(1)
                    filled = sp.shoot_position(filled, computer_shoot)
                    time.sleep(2)
                    if not sl.ships_left(filled_computer):
                        print("\n💀💥 You sunk all the computer's ships! 💥💀")
                        print("🏆 YOU WIN! 🏆")
                        break
                    turn = 2
                else:
                    print("🌊 Your Board 🌊")
                    ccb.cool_board(filled)
                    shoot_coords = []
                    
                    n = len(filled_computer)
                    value = input("\n\nYour turn to shoot (row,col): ")
                    shoot_coords = list(map(int, value.split(",")))

                    if not (0 <= shoot_coords[0] < n and 0 <= shoot_coords[1] < n):
                        print("⚠️ That position doesnt exist. Try again.")
                        continue
                    
                    filled_computer = sp.shoot_position(filled_computer, shoot_coords)
                    if not sl.ships_left(filled):
                        print("\n💀💥 The computer sunk all your ships! 💥💀")
                        print("🏆 COMPUTER WINS! 🏆")
                        break
                    turn = 1
            break
            
        except ValueError as e:
            print(f"❌ Error: {e}. Try again.")

main()