board = list('     \n  1|2|3\n       \n     \n  4|5|6\n       \n     \n  7|8|9\n       \n')
win_cmbos = [{1, 2, 3}, {4, 5, 6}, {8, 9, 7}, {9, 3, 6}, {8, 2, 5}, {1, 4, 7}, {3, 5, 7}, {1, 5, 9}]

def prints():
    print(''.join(board))

def record(board, entry, counter):
    #records player inputs on board
    for char in board:
        try:                           
            char = int(char)        #finds integer in board str
            if char == entry:       
                finder = board.index(str(char))
                if counter%2 == 0:          
                    board[finder] = 'X'        
                else: 
                    board[finder] = 'O'
            
        except ValueError:
            continue

def winner(entries, combos):
    #associates inputs with player and determins winner
    if len(entries) >= 5:           
        plyr1 = set([entries[n] for n in range(0, len(entries), 2)])
        plyr2 = set([entries[n] for n in range(1, len(entries), 2)])
        for combo in combos:
            if combo == plyr1 or combo.issubset(plyr1):
                return 'Player 1 (X) wins'
            elif combo == plyr2 or combo.issubset(plyr2):
                return 'Player 2 (O) wins'

def game():
    entries = []
    i = 0
    while i < 9:
        prints()
        entry = int(input('>Pick a number (1-9)\n'))
        record(board, entry, i)
        entries.append(entry)
        outcome = winner(entries, win_cmbos)
        if type(outcome) == str:
            prints()
            print(outcome)
            break
        
        i += 1

        if i == 9:
            print('It is a draw')

game()
