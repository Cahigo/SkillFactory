def grid_print(val):
    print("| {} | {} | {} |".format(val[0], val[1], val[2]))
    print("----------------")
    print("| {} | {} | {} |".format(val[3], val[4], val[5]))
    print("----------------")
    print("| {} | {} | {} |".format(val[6], val[7], val[8]))


def game_over(player, positions):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]]  # Diagonals
    for i in wins:
        if all(j in positions[player] for j in i):
            return True
    return False


def choice_test(val, player):
    while True:
        try:
            choice = int(input("{}, choose position (1-9):".format(player)))
        except ValueError:
            print("Invalid position")
            continue
        if choice < 1 or choice > 9:
            print("Invalid position")
            continue
        elif val[choice - 1] != " ":
            print("Position is already used")
            continue
        else:
            break
    return choice


def gameplay():
    player = "X"
    val = [" " for i in range(9)]  # Grid's values
    positions = {"X": [], "O": []}  # Player's positions
    for i in val:
        choice = choice_test(val, player)
        val[choice - 1] = player
        positions[player].append(choice - 1)
        grid_print(val)
        if game_over(player, positions):
            print(player, " won!")
            break
        elif i == 9:
            print("Draw!")
        if player == "X":
            player = "O"
        else:
            player = "X"


# -----------------------------------------
while True:
    gameplay()
    retry = input("Another game? (Y/N)")
    if (retry != "Y") or (retry != "y"):
        break
