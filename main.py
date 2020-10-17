cells = [' '] * 9
coordinate_list = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
player = 'X'
while True:
    print('---------')
    print('|', ' '.join(cells[:3]), '|')
    print('|', ' '.join(cells[3:6]), '|')
    print('|', ' '.join(cells[6:]), '|')
    print('---------')
    straights = [cells[:3], cells[3:6], cells[6:], cells[0:7:3], cells[1:8:3], cells[2:9:3], cells[0:9:4], cells[2:7:2]]
    if ['X', 'X', 'X'] in straights:
        print("X wins")
        exit()
    elif ['O', 'O', 'O'] in straights:
        print("O wins")
        exit()
    elif ' ' not in cells:
        print("Draw")
        exit()
    coordinate_x, coordinate_y = input("Enter the coordinates: ").split()
    if coordinate_x.isdigit() and coordinate_y.isdigit():
        if int(coordinate_x) in range(1, 4) and int(coordinate_y) in range(1, 4):
            if cells[coordinate_list.index(coordinate_x + coordinate_y)] == ' ':
                cells[coordinate_list.index(coordinate_x + coordinate_y)] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    else:
        print("You should enter numbers!")
        continue
