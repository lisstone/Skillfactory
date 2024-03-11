import random
#Выбор символа
while True:
    playerSymbol = input("Выбери чем быдешь играть 0 или X: ").upper()
    if playerSymbol == "0":
        print(f"Ваш символ: {playerSymbol}")
        AISymbol = "X"
        break
    elif playerSymbol == "X":
        print(f"Твой символ: {playerSymbol}")
        AISymbol = "0"
        break
    else:
        print(f"Не корректный символ: {playerSymbol}")

gametable = [[" ","0","1","2"],
             ["0","-","-","-"],
             ["1","-","-","-"],
             ["2","-","-","-"]]
#Генерация сетки
def generateTable(table):
    for i in table:
        a = ""
        for j in i:
            a += "  " + a.join(j)
        print(a)

#Ход компа
def AI():
    while True:
        x = random.randint(1,3)
        y = random.randint(1,3)
        if gametable[x][y] == "-":
            gametable[x][y] = AISymbol
            generateTable(gametable)
            break

def player():
    while True:
        y = int(input("Введи номер строки: ")) + 1
        x = int(input("Введи номер колонны: ")) + 1
        if gametable[x][y] == "-":
            gametable[x][y] = playerSymbol
            break
        else:
            print("Введен неверные координаты попробуй еще раз!")
def winner():
    # поиск значений по строке
    for strok in gametable:
        if strok[1] != "-" and strok[1] == strok[2] and strok[1] == strok[3]:
            return True
    # поиск значений по столбу
    for vol in range(1,4):
        stolb = []
        for stl in range(1,4):
            stolb += gametable[stl][vol]
        if stolb[0] != "-" and stolb[0] == stolb[1] and stolb[0] == stolb[2]:
            return True
    # поиск значений по диагонали слево
    tabledig = []
    for dig in range(1,4):
        tabledig += gametable[dig][dig]
    if tabledig[0] != "-" and tabledig[0] == tabledig[1] and tabledig[0] == tabledig[2]:
        return True
    # поиск значений по диагонали справо
    tabledig2 = []
    f = 3
    for dig in range(1, 4):
        tabledig2 += gametable[dig][f]
        f-=1
    if tabledig2[0] != "-" and tabledig2[0] == tabledig2[1] and tabledig2[0] == tabledig2[2]:
        return True
    # проверка на ничью
    SGT = ""
    for i in gametable:
        for j in i:
            SGT += j
    if "-" in SGT:
        return False
    else:
        return True
#Цикл игры
GameExit = False
while GameExit == False:
    AI()
    GameExit = winner()
    if GameExit == False:
        player()
    else:
        break
    GameExit = winner()

print("Конец игры!!!")
generateTable(gametable)