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

"""
1.

a = 6, b = 5, c = 4
a > b is true, so print "one"
c < b is trye, so print "three"

C. "one" and "three"

2. A. 5 7 7

3. C. 1 2 4

4. D. [1,2,3,4] and [1,2,3,[5]]

5. B. dict_keys)['a;' 'b', 'c', 'd']
"""

# 6a

def get_tokens(s:str) -> list[str]:
    """
    tokenise the string. the boundary between 2 tokens is when there are 2 consecutive non-whitespace characters.
    Each token is either single non-whitespace character with or without a prefix of whitespace characters.     
    e.g 
    "ban ana" -> ["b", "a", "n a", "n", "a"]
    "ba n  ana" -> ["b", "a n  a", "n", "a"]
    """
    # removed enclosing whitespace from s
    s = s.strip()

    i = 0
    tokens = []
    token = ""
    previous = ""
    while i < len(s):
        # a new token ia formed if 2 consecutive non-whitespace characters are detected
        # we are supposed to insert a white space between 2 consecutive non-whitespace characters
        if previous != " " and s[i] != " ":
            # the first character of s will always fail the condition of (previous != " " and s[i] != " ")
            # because s[0] is not a white space.
            if len(token) > 0:
                tokens.append(token)
            token = s[i]
        else:
            token += s[i]
        previous = s[i]
        i += 1
    if len(token) > 0:
        # add the last token
        tokens.append(token)
        token = ""
    return tokens

def insertSpaces(s:str) -> str:
    """
    The code works in 2 stages.

    The first stage is tokenise string s into a list of tokens.
    
    The second stage is then to join the tokens together, separated by a white space.
    """
    tokens = get_tokens(s)
    return " ".join(tokens)

# 6b

def q6b():
    """
    The menu program is based on a sentinel loop
    """
    while True:
        word = input("Enter a word (Press enter to exit): ").strip()
        if len(word) == 0:
            # quits the program if user didn't enter any word
            print("Program terminated")
            break
        else:
            # insert spaces into the word, then print the result
            print(insertSpaces(word) + "\n")
    
# 7a

def encode(morseMapping: dict[str,str], character:str) -> str:
    return morseMapping.get(character, "#")

# 7b 

def textToMorse(morseMapping:dict[str,str], infile:str, outfile:str) -> None:
    with (open(outfile,"w") as f, open(infile) as g):
        # open outfile to write, open infile to read
        for line in g:
            # remove the enclosed and trailing white spaces of each new line
            line = line.strip()
            encoded = []
            for c in line:
                # encode each character of every line
                encoded.append(encode(c))
            # insert space between morse codes
            # then write the encoded line to the output file
            print(" ".join(encoded), file=f)

# 8

import random 

def q8():
    score = 21 
    print(f"Seed score: {score}")
    i = 0
    roll = 0
    while score > 0:
        # a new round starts as long as the seed score > 0
        # roll the dice repeatedly as long as the dice value exceeds the seed score
        toRoll = True
        while toRoll:
            roll = random.randint(1,6)
            i += 1
            toRoll = roll > score
        score -= roll
        print(f"Roll: {i} ... Seed Score now: {score}")
    print("Game Over")

# 9

import random

def q9():
    players = ["Tom", "Jim", "Dan"]
    score = {"Tom": [21,21,21], "Jim":[21,21,21], "Dan":[21,21,21]}
    for r in range(3):
        print(f"Round {r + 1}")

        no_round_winner = True 
        round_winner = ""
        while no_round_winner:
            for player in players:
                roll = random.randint(1,6)
                if roll > score[player][r]:
                    print(f"{player} rolls {roll} ... Need to roll again")
                else:
                    score[player][r] -= roll
                    if no_round_winner and score[player][r] == 0:
                        round_winner = player
                        no_round_winner = False
                    print(f"{player} rolls {roll} ... Seed score now: {score[player][r]}")
        print(f"{round_winner} reaches Seed Score: 0! Wins the round")

        print("Updated Scores:")
        print(f"Score = {score}")
        print("\n\n")            

    # compute total score 
    final = {}
    lowest = 63 # max possible score for 3 rounds is 3 x 21 = 63
    for player in players:
        total = sum(score[player])
        final[player] = total
        if total < lowest:
            lowest = total
    # there may be more than 1 winner
    overall_winners = [player for player in players if final[player] == lowest]
    print("Final Scores:")
    print(f"score = {score}")
    print(f"Overall Winner(s): {', '.join(overall_winners)}")
