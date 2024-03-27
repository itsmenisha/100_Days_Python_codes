# code with harry tic tac toe
def printBoard(xstate, ostate):
    one = 'X' if xstate[0] else ('O' if ostate[0] else 0)
    two = 'X' if xstate[1] else ('O' if ostate[1] else 1)
    three = 'X' if xstate[2] else ('O' if ostate[2] else 2)
    four = 'X' if xstate[3] else ('O' if ostate[3] else 3)
    five = 'X' if xstate[4] else ('O' if ostate[4] else 4)
    six = 'X' if xstate[5] else ('O' if ostate[5] else 5)
    seven = 'X' if xstate[6] else ('O' if ostate[6] else 6)
    eight = 'X' if xstate[7] else ('O' if ostate[7] else 7)
    nine = 'X' if xstate[8] else ('O' if ostate[8] else 8)
    print(f"_____|_____|_____")
    print(f"{one}  |  {two}  |  {three}  ")
    print(f"_____|_____|_____")
    print(f"{four}  |  {five}  |  {six}  ")
    print(f"_____|_____|_____")
    print(f"{seven}  |  {eight}  |  {nine}  ")


def sum(a, b, c):
    return a+b+c


def checkWin(xstate, ostate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("X won!!!!!")
            return 1
        if (sum(ostate[win[0]], ostate[win[1]], ostate[win[2]]) == 3):
            print("O won!!!!!")
            return 0
    return -1


if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ostate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    trun = 1  # 1 for x o for y
    print("lets start the game")
    while (True):
        printBoard(xstate, ostate)
        if (trun == 1):
            print("its X's chance")
            value = int(input("enter the place you would like(0 to 8) :"))
            xstate[value] = 1
        else:
            print("its O's chance")
            value = int(input("enter the place you would like(0 to 8) :"))
            ostate[value] = 1
        cwin = checkWin(xstate, ostate)
        if (cwin != -1):
            print("match over")
            printBoard(xstate, ostate)
            break
        trun = 1-trun


# list = ["1", "2", "3"]
# row1 = ["  ", " ", " "]
# row2 = ["  ", " ", " "]
# row3 = ["  ", " ", " "]
# print (f"1{row1}\n2{row2}\n3{row3}")
# print(" ")
# print(list)
# print(map)
# position = input("enter the position you want the treasure to be searched at: ")
# hor = int(position[0])
# ver = int(position[1])
# print(" ")
# print(list)
# map[ver-1][hor-1]=x
# print (f"1{row1}\n2{row2}\n3{row3}")
