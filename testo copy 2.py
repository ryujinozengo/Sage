import random
import PROJ_Text_to_speech

board = [' ' for x in range(10)]
board[0]='#'

def insertLetter(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '

def isBoardFull(board):
    if(board.count(' ')==0):
        return True
    else:
        return False

def printBoard(board):
    print()
    print("-------------------------")
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('   |   |   ')
    print("------------------------")
    print()

def IsWinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or (b[4]==l and b[5]==l and b[6]==l) or
            (b[7]==l and b[8]==l and b[9]==l) or (b[1]==l and b[4]==l and b[7]==l) or
            (b[2]==l and b[5]==l and b[8]==l) or (b[3]==l and b[6]==l and b[9]==l) or
            (b[1]==l and b[5]==l and b[9]==l) or (b[3]==l and b[5]==l and b[7]==l))

def playerMove():
    while True:
        print("Please select a position to enter the X between 1 to 9 :- ")
        PROJ_Text_to_speech.speech("Please enter your move")
        move = input()
        print("-----------")
        
        try:
            move = int(move)
            if (move > 0 and move < 10):
                if spaceIsFree(move):
                    insertLetter('X' , move)
                    break
                else:
                    print('Sorry, this space is occupied')
                    PROJ_Text_to_speech.speech("The place is occupied")
            else:
                print('Please type a number between 1 and 9 :-')
                PROJ_Text_to_speech.speech("Type a number between 1 and 9")

        except:
            print('Please type a number')
            PROJ_Text_to_speech.speech("Please type a number")
            playerMove()

def computerMove():
    possibleMoves=[]
    for i in range(len(board)):
        if(board[i]==' '):
            possibleMoves.append(i)
    move=0

    for j in ['O','X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i]=j
            if IsWinner(boardcopy,j):
                move=i
                return move

    if((board[1]=='X' and board[5]=='O' and board[9]=='X')or(board[3]=='X' and board[5]=='O' and board[7]=='X')):
        edgesOpen=[]
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)
        if len(edgesOpen)>0:
            return random.choice(edgesOpen)
        cornerOpen=[]
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornerOpen.append(i)
        if len(cornerOpen)>0:
            return random.choice(cornerOpen)
    
    if 5 in possibleMoves:
        move=5
        return move
    
    cornerOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen)>0:
        return random.choice(cornerOpen)
    
    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        return random.choice(edgesOpen)

def ttt():
    print()
    print("WELCOME TO TIC-TAC-TOE")
    print("------------------------------------------")
    PROJ_Text_to_speech.speech("Welcome to tic tac toe")
    printBoard(board)
    while not(isBoardFull(board)):
        if not(IsWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print("You lose!")
            PROJ_Text_to_speech.speech("You lose")
            break

        if not(IsWinner(board,'X')):
            move=computerMove()
            if(move==None or move==0):
                print("")
            else:
                insertLetter('O',move)
                print("Computer placed O in position ",move)
                printBoard(board)
                PROJ_Text_to_speech.speech("Computer made is move in position"+str(move))
        else:
            print("You win")
            PROJ_Text_to_speech.speech("Congratulations You win")
            break

    if isBoardFull(board):
        print("Tie game")
        PROJ_Text_to_speech.speech("The matched ended in a draw")

ttt()