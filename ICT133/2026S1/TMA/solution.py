from typing import Tuple 

def q1() -> None:
    """
    enter password
    if password is valid then

        reenter password

        if passwords match then
            print "password is accepted"
        else
            print "Unable to accept - passwords don't match"

    else

        display error message for each error detected

        if pasword length insufficient then
            print "Invalid password - Min length is 8"
        if password does not contain special charactrs
            print "Invalid password - Missing @ or #"
        if first character is not uppercase alphabet
            print "Invalid password - First character must be an uppercase alphabet"
    """
    password = input("Enter password: ")
    if len(password) >= 8 and ("@" in password or "#" in password) and password[0].isupper():
        reenter = input("Re-enter password: ")
        if reenter == password:
            print("Password is accepted")
        else:
            print("Unable to accept password - passwords don't match.")
    else:
        if not len(password) >= 8:
            print("Invalid Passowrd - Min length is 8")
        if not ("@" in password or "#" in password):
            print("Invalid password - Missing @ or #")
        if not password[0].isupper():
            print("Invalid Password - First character should xbe an uppercase alphabet")
        
# question 2a

def first_char(text:str, char:str) -> int:
    """
    Identify the index of the first occurence of char in text
    if char not found, returns -1

    search for char from the start of the text

    for i = 0 to n-1 where n is the length of text
        if text[i] matches char
            return i
    return -1 because char is not found
    """
    for i in range(len(text)):
        if text[i] == char:
            return i
    return -1 

def last_char(text:str, char:str) -> int:
    """
    Identify the index of the last occurence of char
    if char not found, returns -1

    search for char from the back of text

    for i = (n-1) to 0 where n is the length of text
        if text[i] matches char
            return i
    
    return n since char not found
    """
    for i in range(len(text)-1,-1,-1):
        if text[i] == char:
            return i 
    return -1


def countCharsBetween(text:str, char:str) -> int:
    """
    counts the number of unique characters between `char` in `text`

    if char is invalid then
        return -1

    search for enclosing char in text where
        start = index of first char in text [-1 if char is not in text]
        stop = index of last char in text [len(text) if char is not in text]

    search has 3 outcomes

    if no occurence of char then
        return -1

    if single occurence of char then
        return -1
        
    if enclosing char are found

        if empty string between start and stop then
            return 0
        else
            subtext = text[start+1:stop]
            remove white space from subtext
            sort subtext
            sorting will cluster all the same characters together
            e.g. "abcabcabc" -> "aaabbbccc"
            
            count = 1
            for every 2 adjcant characters in subtext that are different
                count += 1
            return count

    """
    if not(len(char) == 1 and not char.isspace()):
        return -1 
    
    start = first_char(text, char)
    stop = last_char(text, char)

    if start == -1:
        return -1 
    elif start == stop:
        return -1
    else:
        # enclosing char found

        # empty string between enclosing char
        if start + 1 == stop:
            return 0
        else:
            # non-empty string between enclosing char
            subtext = sorted([c for c in text[start+1:stop] if not c.isspace()])
            count = 1
            for i in range(1, len(subtext)):
                if subtext[i] != subtext[i-1]:
                    count += 1
            return count 

def q2b() -> None:
    """
    menu program for a2b/

    do until user terminated program
        enter text 
        if user enters exit
            print "terminating program"
            terminate program
        else:
            enter char 
            n = countCharsBetween(text, char)
            if n == -1 then
                print error message
            else
                print f"There are {n} unique character between the first and last `{char}` in `{text}`"
    """
    user_terminates = False
    while not user_terminates:
        text = input("Enter text (press <ENTER> to exit): ")
        if text == "":
            print("Terminating program")
            user_terminates = True
        else:
            char = input("Enter character: ")
            n = countCharsBetween(text, char)
            if n == -1:
                print(f"`{char}` should be a repeated single non-whitespace character in `{text}`")
            else:
                print(f"There are {n} unique character between the first and last `{char}` in `{text}`")

# question 3

def hasTwoChars(text:str) -> bool:
    """
    checks if text contains at least 2 repeating characters

    remove white space from text
    if length of text < 2
        return False    
    sort text
    if any 2 adjacent character of text are the same
        return True
    return False
    """
    L = [c for c in text if not c.isspace()]
    if len(L) < 2:
        return False
    L = sorted(L)    
    for i in range(1,len(L)):
        if L[i] == L[i-1]:
            return True
    return False


def to_ask(round_no:int, p:int, text:str) -> Tuple[int,str]:
    """
    keeps on asking for char until the score is accepted

    do until score is accepted
        ask player p for char
        calculate score
        if score == -1
            print error message
        else
            acccept score
    return score, char
    """
    score_accepted = False 
    while not score_accepted:
        char = input(f"Round {round_no}: Player {p}, Enter a character from `{text}: `")
        score = countCharsBetween(text,char)
        if score == -1:
            print(f"Error. `{char}` must be a repeated single non-whitespace character inside `{text}`")
        else:
            score_accepted = True 
    return score, char

def q3b() -> None:
    """
    for each game
        enter text
        scores = []

        round_no = 0
        for each round
            round_no += 1    
            if text has at least 2 repeating characters then
                ask for char and calculate score
                append score to scores
                print f"There are {score} unique letters between first and last {char}. You scored {score} points."
                update text with text[first_char+1:last_char] where
                    first_char is the index of the first occurence of char in text
                    last_char is the index of the last occurence of char in text
            else
                print f"{text} has no more repeating characters"
                end all rounds and game    
        print game summary
    """
    next_game  = True
    while next_game:
        scores: list[int] = [ ]        
        text = input("Please enter text: ")
        next_round = True
        round_no = 0 
        while next_round:
            round_no += 1
            if hasTwoChars(text):
                score, char = to_ask(round_no, 1, text)
                print(f"There are {score} unique letters between first and last {char}. You scored {score} points.")
                scores.append(score)
                text = text[first_char(text,char)+1:last_char(text,char)]
            else:
                print(f"`{text}` has no more repeating characters")
                next_round = False 
                next_game = False
            
        for i in range(len(scores)):
            print(f"Round {i+1}, Score {scores[i]}")
        print(f"Total Score: {sum(scores)}")

def ask_text() -> str:
    """
    Asks for text

    do until text is accepted
        text = ask user for text
        if text contains at least 2 repeating characters
            accept text
        else
            print error message
    return text
    """
    text_accepted = False 
    while not text_accepted:
        text = input("Enter text: ")
        if hasTwoChars(text):
            text_accepted = True
        else:
            print("Text has no repeating characters")
    return text

def ask_n_players() -> int:
    """
    Asks user for number of players

    do until n is accepted
        n = ask user for 2-5 players
        if 2 <= n <= 5 then
            accept n
        else
            print error message
    return n
    """
    n_accepted = False 
    while not n_accepted:
        n = int(input("Enter number of players (2-5): "))
        if 2 <= n <= 5:
            n_accepted = True 
        else:
            print("Enter a number between 2 and 5")
    return n 
 
def q4() -> None:
    """
    Menu system for question 4

    text = asks for text
    n = ask for number of players (2-5)

    initialise texts and scores
    texts = [text] * n
    scores = [0] * n

    for each game
        for each round
            for each player
                if player's text has at least 2 repeating characters
                    ask player for char                                                                                                                                                                                                                                         
                    calculate score 
                    update player's total score
                    update player's text with text[first_char+1:last_char] where
                        first_char is the index of the first occurence of char in text
                        last_char is the index of the last occurence of char in text
                else
                    print "player's text has no more valid characters"
        
            
            if all players' texts have no repeating characters
                end all rounds and game
    
        print game summary

    """

    text = ask_text()
    n = ask_n_players()

    texts = [text] * n 
    scores = [0] * n

    next_game = True 
    while next_game:
        round_no  = 0
        next_round = True 
        while next_round:
            round_no += 1
            all_texts_no_repeating_char= True
            for p in range(n):
                if hasTwoChars(texts[p]):
                    all_texts_no_repeating_char = False
                    score, char = to_ask(round_no, p+1, texts[p])
                    scores[p] += score 
                    texts[p] = texts[p][first_char(texts[p], char)+1:last_char(texts[p],char)]
                    print(f"Great! You scored {score} points, total score {scores[p]} points")
                else:
                    print(f"Player {p+1}'s text has no more valid characters.")

            
            if all_texts_no_repeating_char:
                next_game = False
                next_round = False 
        
        for p in range(n):
            print(f"Player {p+1} scored {scores[p]} points")



