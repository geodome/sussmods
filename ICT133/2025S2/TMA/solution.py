"""
Author: Donaldson Tan

If you need tuition, feel free to contact me at 
maths_and_programming@outlook.sg.  

If you don't understand the solutions provided, you may 
consult me at @geodome via Telegram.  

I provide tuition for the following SUSS undergraduate modules:  

* BUS105  Statistics
* ENG301  Microprocessor Programming  
* EAS439  Numerical Analysis
* ICT133  Structured Programming  
* ICT162  Object Oriented Programming    
* ICT235  Data Structures and Algorithms
* ICT325  Algorithm Design and Analysis
* ICT330  Database Management Systems
* MTD215  Application of C++ in Multimedia
* MTD315  Computer Interactive Graphics
* MTH105  Fundamentals of Mathematics  
* MTH109  Calculus  
* MTH207  Linear Algebra  
* MTH210  Fundamentals of Probability
* MTH212  Statistical Analysis
* MTH240  Engineering Mathematics I
* MTH316  Multivariable Calculus  
* MTH321  Engineering Mathematics II
* MTH355  Basic Mathematical Optimisation
* MTH357  Applied Regression Analysis I
"""

from typing import Tuple

def q1a() -> None:

    n = 0
    while True:  
        n = int(input("Enter size of board (3-9, odd): "))
        if n in [3,5,7,9]:
            break
        else:
            print("Invalid board size. Please enter an odd integer between 3 and 9.")
    
    # assume valid input
    row = int(input(f"Enter row number (1 to {n}): "))
    col = int(input("Enter column number (1 to {n}): "))

    # resolve the color using linear inequality involving the diagonal and antidiagonal
    if row < col:
        if row < n + 1 - col:
            print("Color is Green")
        elif row > n + 1 - col:
            print("Color is Blue")
        else:
            print("No Color")
    elif row > col:
        if row > n + 1 - col:
            print("Color is Red")
        elif row < n + 1 - col:
            print("Color is Yellow")
        else:
            print("No Color")
    else:
        print("No Color")

def q1b() -> None:
    """
    Use the same linear inequality strategy to solve the problem
    However, each color region is defined by a unique linear inequality
    """

    n = 0
    while True:  
        n = int(input("Enter size of board (4-10, odd): "))
        if n in [4,6,8,10]:
            break
        else:
            print("Invalid board size. Please enter an odd integer between 3 and 9.")
    
    # assume valid input
    row = int(input(f"Enter row number (1 to {n}): "))
    col = int(input("Enter column number (1 to {n}): "))

    if row <= n//2 + 1 - col:
        print("Color is Blue")
    elif row >= n + n//2 + 1 - col:
        print("Color is Red")
    elif row <= col - n//2:
        print("Color is Blue")
    elif row >= col + n//2:
        print("Color is Yellow")
    else:
        print("No Color")

# Question 2(a)

def getColor(n:int, row:int, col:int) -> str:
    if row <= n//2 + 1 - col:
        return "G"
    elif row >= n + n//2 + 1 - col:
        return "R"
    elif row <= col - n//2:
        return "B"
    elif row >= col + n//2:
        return "Y"
    else:
        return "-"

# Question 2(b)

def q2b() -> None:
    # prompt for board size
    n = 0 
    while True:
        n = int(input("Enter size of board (4-10, even): "))
        if n in [4,6,8,10]:
            break
        else:
            print("Invalid board size. Please enter an even integer between 4 and 10.")
    
    # to display the board
    for row in range(1,n+1):
        for col in range(1,n+1):
            print(getColor(n,row,col),end="")
        print()
    print()

# Question 2(c)

def getColor2c(n:int, row:int, col:int) -> str:
    # use linear ineqality to determine the color
    if row <= n//2 + 1 - col:
        return "G"
    elif row >= n + n//2 + 1 - col:
        return "R"
    elif row <= col - n//2:
        return "B"
    elif row >= col + n//2:
        return "Y"
    else:
        # the number 'ring' corresponds to a unique distance function in each quadrant
        if col > n // 2:
            if row > n // 2:
                # red quadrant
                return str((n + n//2 + 1 - col) - row)
            else:
                # blue quadrant
                return str(row - (col - n//2))
        else:
            if row > n // 2:
                # yellow quadrant
                return str((col + n//2) - row)
            else:
                # green quadrant
                return str(row - (n//2 + 1 - col))
    
def q2c() -> None:
    # prompt for board size
    n = 0 
    while True:
        n = int(input("Enter size of board (4-10, even): "))
        if n in [4,6,8,10]:
            break
        else:
            print("Invalid board size. Please enter an even integer between 4 and 10.")
    
    # to display the board
    for row in range(1,n+1):
        for col in range(1,n+1):
            print(getColor2c(n,row,col),end="")
        print()
    print()

# Question 3

import random

def getPlayers() -> list[str]:
    players = []
    unique_names = [] 
    while True:
        player = input(f"Enter player {len(players)+1}'s name (empty to end): ")
        if player == "":
            if len(players) < 2:
                print("Please enter at least 2 players.")
            else:
                return players
        if player.lower() in unique_names:
            print("repeated name. please try again.")
        else:
            unique_names.append(player.lower())
            players.append(player)
            # max 5 players
            if len(players) == 5:
                return players

def is_win(score:int, m:int, n:int) -> bool:
    return score == 0 and m == 2

def is_bust(score:int, m:int, n:int) -> bool:
    return score < 0 or (score == 0 and m != 2) or score == 1

def q3() -> None:
    multiplier = ["", "single", "double", "triple"]

    # Prompt for players' names
    players = getPlayers()

    # each game consist of turns. each turn consist of rounds.
    next_game = True
    while next_game:
        # reset the game
        random.shuffle(players)
        scores = [501] * len(players)
        turns = [0] * len(players)
        i = -1

        next_turn = True
        while next_turn:
            
            # pick player i
            i = (i + 1) % len(players)
            turns[i] += 1
            print(f"{players[i]}'s turn {turns[i]}, current score is {scores[i]}")
            initial_score = scores[i]

            # each turn has a max of 3 rounds
            for round in range(1,4):
                # assumes valid input
                n = int(input(f"{players[i]}'s round {round}, choose a number form 1 to 20 inclusive, or 25: "))
                # determine multiplier
                if n == 25:
                    m = random.randint(1,2)
                else:
                    # 1 <= n <= 20
                    m = random.randint(1,3)
                # update score then determine outcome
                scores[i] -= m*n
                if is_win(scores[i], m, n):
                    # 1st outcome is win
                    # terminate game if win
                    next_turn = False 
                    next_game = False
                    print(f"It is a {multiplier[m]}, total {m}x{n} points, {players[i]} wins in {turns[i]} turns.")
                    break
                elif is_bust(scores[i], m, n):
                    # 2nd outcome is bust
                    # if bust, revert score and move to next player
                    scores[i] = initial_score
                    print(f"It is a {multiplier[m]}, total {m}x{n} points, {players[i]} is bustedm reverting to initial score of {scores[i]}.")
                    break 
                else:
                    # 3rd outcome is next round
                    print(f"It is a {multiplier[m]}, total {m}x{n} points, {players[i]}'s new score is {scores[i]}.")
            
            if next_turn:
                print("Next player...")

        # display end-of-game summary
        for i in range(len(players)):
            print(f"{players[i]}'s score is {scores[i]}")    

# Question 4(a)

def setup_seating_plan() -> Tuple[list[list[str]], list[int], bool]:
    while True:
        rows = int(input("Enter number of rows (3-10 inclusive, 0 to quit): "))
        if 3 <= rows <= 10:
            break
        elif rows == 0:
            return [], [], [], True
        else:
            print("invalid number of rows")
    
    while True:
        cols = int(input("Enter number of columns (3-10 inclusive, 0 to quit): "))
        if 3 <= cols <= 10:
            break
        elif cols == 0:
            return [], [], [], True
        else:
            print("invalid number of columns")

    plan = [] 
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("O")
        plan.append(row)
    return plan, [cols]*rows, False


def display_menu() -> None:
    print("Booking Menu")
    print("============")
    print("1. Show seats")
    print("2. Book seats")
    print("0. Quit")
    print()

def show_seats(seating_plan:list[list[str]]) -> None:
    rows = len(seating_plan)
    cols = len(seating_plan[0])

    print("  " + "SCREEN".center(3*cols))
    print()

    # print header
    header_cols = [chr(ord('A') + i).ljust(3) for i in range(cols)]
    header = "   " + "".join(header_cols)
    print(header)
    
    for i in range(rows):
        # start printing each row
        print(str(i+1).rjust(2,"0"), end=" ")
        for j in range(cols):
            print(seating_plan[i][j].ljust(3, " "), end="")
        print()
    
    print()

def correct_format(seats:str) -> bool:
    return len(seats) > 4 and seats[0].isalpha() and seats[1:3].isdigit() and seats[3] == "-" and seats[4:].isdigit()

def parse_seats(seats:str) -> Tuple[bool, int, int, int]:
    valid_format, row, col, n = False, -1, -1, -1
    if correct_format(seats):
        valid_format = True
        col = ord(seats[0].upper()) - ord('A')
        row = int(seats[1:3])-1
        n = int(seats[4:])
    return valid_format, row, col, n

def is_available(seating_plan: list[list[str]], row:int, col:int, n:int) -> bool:
    cols = len(seating_plan[0])
    if col + n - 1 >= cols:
        return False
    for i in range(n):
        if seating_plan[row][col+i] == "X":
            return False
    return True
       
def book_seats(seating_plan:list[list[str]], nseats:list[int]) -> None:
    rows = len(seating_plan)
    cols = len(seating_plan[0])

    show_seats(seating_plan)

    seats = input("Enter seats to book (format @NN-#): ").upper()
    valid_format, row, col, n = parse_seats(seats)
    if valid_format:
        if not -1 < row < rows:
            print("Invalid row. Try again.")
        elif not -1 < col < cols:
            print("Invalid seat label. Try again.")
        elif not 0 < n <= nseats[row]:
            print("Invalid number of seats. Try again.") 
        elif is_available(seating_plan, row, col, n):
            # add booking
            for i in range(n):
                seating_plan[row][col + i] = "X"
            nseats[row] -= n
            print(f"{n} Seats booked.")
        else:
            print("Not all seats are available. Try again.")
    else:
        print("Invalid input! Please enter in @NN-# format")


def q4a() -> None:
    # Setup seating plan 
    seating_plan, nseats, to_quit = setup_seating_plan()
    print()

    if not to_quit:
        # begin menu loop
        while True:
            display_menu()
            opt = int(input("Enter option: "))
            print()
            if opt == 0:
                break 
            elif opt == 1:
                show_seats(seating_plan)
            elif opt == 2:
                book_seats(seating_plan, nseats)
            else:
                print(f"invalid option {opt}")
            print()

    print("Program end.")

# Question 4(b)

def display_menu_b() -> None:
    print("Booking Menu")
    print("============")
    print("1. Show seats")
    print("2. Book seats")
    print("3. Auto select seats")
    print("0. Quit")
    print()

def setup_seating_plan_b() -> Tuple[list[list[str]], list[int], list[list[list[int]]], bool]:
    seating_plan, nseat, all_blocks, to_quit = [], [], [], False
    while True:
        rows = int(input("Enter number of rows (3-10 inclusive, 0 to quit): "))
        if 3 <= rows <= 10:
            break
        elif rows == 0:
            return [], [], [], True
        else:
            print("invalid number of rows")
    
    while True:
        cols = int(input("Enter number of columns (3-10 inclusive, 0 to quit): "))
        if 3 <= cols <= 10:
            break
        elif cols == 0:
            return [], [], [], True
        else:
            print("invalid number of columns")

    nseat = [cols] * rows
    for i in range(rows):
        all_blocks.append([[0, cols-1]])
        row = []
        for j in range(cols):
            row.append("O")
        seating_plan.append(row)
    return seating_plan, nseat, all_blocks, to_quit


def distance_from_mid(block:list[int], mid:int) -> int:
    i, j = block
    if i <= mid <= j:
        return 0
    return min(abs(i-mid), abs(j-mid))

def can_contain(block:list[int], n:int) -> bool:
    i, j = block 
    return j - i + 1 >= n

def contains(block:list[int], col:int, n:int) -> bool:
    i, j = block
    return i <= col <= col+n-1 <= j

def book_seats_b(seating_plan:list[list[str]], nseats:list[int], alL_blocks:list[list[list[int]]]) -> None:
    rows = len(seating_plan)
    cols = len(seating_plan[0])

    show_seats(seating_plan)

    seats = input("Enter seats to book (format @NN-#, 0 to cancel): ").upper()
    if seats == "0":
        return
    valid_format, row, col, n = parse_seats(seats)
    if valid_format:
        if not -1 < row < rows:
            print("Invalid row. Try again.")
        elif not -1 < col < cols:
            print("Invalid seat label. Try again.")
        elif not 0 < n <= nseats[row]:
            print("Invalid number of seats. Try again.") 
        else:
            blocks = alL_blocks[row]
            for i in range(len(blocks)):
                if contains(blocks[i], col, n):
                    update_blocks(blocks, i, col, col+n-1)
                    for l in range(col, col+n):
                        seating_plan[row][l] = "X"
                        nseats[row] -= 1     
                    print(f"{n} seats are booked.")              
                    break
            else:
                print("Not all seats are available.")
    else:
        print("Invalid input! Please enter in @NN-# format")

def to_accept(seating_plan:list[list[int]], nseats:list[int], row:int, i:int, j:int) -> Tuple[bool,bool]:
    show_seats(seating_plan)
    prompt = f"Do you accept {chr(ord('A')+i)}{str(row+1).rjust(2,'0')} to {chr(ord('A')+j)}{str(row+1).rjust(2,'0')}? (Y/N, 0 to cancel) "
    if i == j:
        prompt = f"Do you accept {chr(ord('A')+i)}{str(row+1).rjust(2,'0')}? (Y/N, 0 to cancel ) "
    response = input(prompt).upper()
    print()
    accepted = response == "Y"
    cancelled = response == "0"
    if accepted:
        for o in range(i, j+1):
            seating_plan[row][o] = "X"
            nseats[row] -= 1
    return accepted, cancelled

def block_subtract(A:list[int], B:list[int]) -> list[list[int]]:
    # assumes block B is a subset of block A
    result = []
    i, j = A
    k, l = B
    m, n = i, k-1 
    if n >= m:
        result.append([m,n])
    o, p = l+1, j
    if p >= o:
        result.append([o,p])
    return result

def update_blocks(blocks:list[list[int]], i:int, l:int, m:int) -> None:
    subtract = block_subtract(blocks[i], [l, m])
    if len(subtract) == 0:
        blocks.pop(i)
    else:
        blocks[i] = subtract[0]
        if len(subtract) > 1:
            blocks.append(subtract[1])

def accepted_from_row(seating_plan:list[list[int]], blocks:list[list[int]], n:int, mid:int, row:int, nseats:list[int]) -> Tuple[bool, bool]:
    accepted = False
    cancelled = False
    candidates = []
    for i in range(len(blocks)):
        block = blocks[i]
        if can_contain(block, n):
            candidates.append((distance_from_mid(block, mid), i, block[0], block[1]))
    candidates.sort()
    while len(candidates) > 0 and not accepted:
        _, i, j, k = candidates.pop(0)
        if j <= mid <= k:
            # grow the selection block from the mid position
            n1 = n - 1
            l, m, grow_m = mid, mid, True 
            while n1 > 0:
                if grow_m:
                    if m < k:
                        m += 1
                        n1 -= 1
                else:
                    if j < l:
                        l -= 1
                        n1 -= 1
                grow_m = not grow_m

            for o in range(k - m + 1):
                accepted, cancelled = to_accept(seating_plan, nseats, row, l+o, m+o)
                if cancelled:
                    return accepted, cancelled 
                if accepted:
                    update_blocks(blocks, i, l+o, m+o)
                    break

            if not accepted:
                for o in range(1, l - j + 1):
                    accepted, cancelled = to_accept(seating_plan, nseats, row, l-o, m-o)
                    if cancelled:
                        return accepted, cancelled
                    if accepted:
                        update_blocks(blocks, i, l-o, m-o)
                        break

        if mid < j:
            l, m = j, j + n - 1
            for o in range(k - m + 1):
                accepted, cancelled = to_accept(seating_plan, nseats, row, l+o, m+o)
                if cancelled:
                    return accepted, cancelled
                if accepted:
                    update_blocks(blocks, i, l+o, m+o)
                    break

        if mid > k:
            l, m = k - n + 1, k
            for o in range(l - j + 1):
                accepted, cancelled = to_accept(seating_plan, nseats, row, l-o, m-o)
                if cancelled:
                    return accepted, cancelled
                if accepted:
                    update_blocks(blocks, i, l-o, m-o)
                    break

    return accepted, cancelled

def auto_select(seating_plan: list[list[int]], nseats:list[int], all_blocks: list[list[list[int]]]) -> None:
    rows = len(seating_plan)
    cols = len(seating_plan[0])
    mid = cols // 2
    # assume valid input n >= 0
    n = int(input("Enter number of seats to book (0 to cancel): "))
    if n == 0:
        return
    # start searching row by row
    for row in range(rows-1,-1,-1):
        blocks = all_blocks[row]
        accepted, cancelled = accepted_from_row(seating_plan, blocks, n, mid, row, nseats)
        if accepted:
            print(f"{n} seats booked.")
            break
        if cancelled:
            return
    else:
        print("No seats are booked.")


def q4b() -> None:
    # Setup seating plan 
    seating_plan, nseats, all_blocks, to_quit = setup_seating_plan_b()
    print()
    if not to_quit:
        # begin menu loop
        while True:
            display_menu_b()
            opt = int(input("Enter option: "))
            print()
            if opt == 0:
                break 
            elif opt == 1:
                show_seats(seating_plan)
            elif opt == 2:
                book_seats_b(seating_plan, nseats, all_blocks)
            elif opt == 3:
                auto_select(seating_plan, nseats, all_blocks)
            else:
                print(f"invalid option {opt}")
            print()

    print("Program end.")
