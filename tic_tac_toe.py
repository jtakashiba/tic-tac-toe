# Tic Tac Toe Game
# Text-based, to be played in the command line
# Date: 04/10/2024

board_pos = ['   ','   ','   ','   ','   ','   ','   ','   ','   ']
game_on = True
turn = 0

# Print empty board at the beginning
print(f"{board_pos[0]}|{board_pos[1]}|{board_pos[2]}\n\
------------\n\
{board_pos[3]}|{board_pos[4]}|{board_pos[5]}\n\
------------\n\
{board_pos[6]}|{board_pos[7]}|{board_pos[8]}\n")

def check_for_winner(player, game_on):
    no_winner = True
    win_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8]]
    for comb in win_combinations:           
        if no_winner:
            if board_pos[comb[0]] == player and board_pos[comb[1]] == player and board_pos[comb[2]] == player:
                no_winner = False
                print(f"Congratulations player{player}, you won!")
                game_on = False
    return game_on

while game_on or turn < 10:
    # Player Input
    player_input = input("Choose your position from 1 to 9 (1 = top left down to 9 = bottom right): \n ")
    player_pos = int(player_input) - 1

    # Check if input is valid    
    if player_pos >= 0 and player_pos < 9:     
        if turn % 2 != 0:
            board_pos[player_pos] = ' X '
        else:
            board_pos[player_pos] = ' O '
        
        print(f"        {board_pos[0]}|{board_pos[1]}|{board_pos[2]}\n\
        ------------\n\
        {board_pos[3]}|{board_pos[4]}|{board_pos[5]}\n\
        ------------\n\
        {board_pos[6]}|{board_pos[7]}|{board_pos[8]}\n")       

        # Check if the player completed the game
        if turn > 0:
            game_on = check_for_winner(board_pos[player_pos], game_on)
        turn += 1
    else:
        print("Your input must be between 1 and 9. Try again!")





