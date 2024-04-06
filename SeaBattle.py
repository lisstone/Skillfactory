import random

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def Xpos(self):
        return self.x

    @property
    def Ypos(self):
        return self.y

class Box:
    CreateBlock = "■"
    DestroyBlock = "X"
    FallBlock = "T"

    @property
    def CreateShipBlock(self):
        return self.CreateBlock

    @property
    def DestroyShipBlock(self):
        return self.DestroyBlock

    @property
    def FallShipBlock(self):
        return self.FallBlock
class Table:
    class GridTable:
        @property
        def gridTable(self):
            self.GridTable = [[" ", "1", "2", "3", "4", "5", "6"],
                              ["1", "O", "O", "O", "O", "O", "O"],
                              ["2", "O", "O", "O", "O", "O", "O"],
                              ["3", "O", "O", "O", "O", "O", "O"],
                              ["4", "O", "O", "O", "O", "O", "O"],
                              ["5", "O", "O", "O", "O", "O", "O"],
                              ["6", "O", "O", "O", "O", "O", "O"], ]
            return self.GridTable

    def __init__(self, name):
        self.name = name
        self.grid = self.GridTable().gridTable

    def SpawnShip(self, length=3, count=1):
        self.length = length
        self.count = count

        while count > 0:
            emyty = False
            xRand = random.randint(1, 6)
            yRand = random.randint(1, 6)

            if yRand > 6-(self.length-1):
                yRand = 6-(self.length-1)

            ship = Ship(xRand,yRand)

            for i in range(self.length):
                if self.grid[ship.Xpos][ship.Ypos+i] != "O":
                    emyty = True

            if ship.Ypos > 1:
                if self.grid[ship.Xpos][ship.Ypos-1] != "O":
                    emyty = True
            if ship.Ypos + (self.length-1) < 6:
                if self.grid[ship.Xpos][ship.Ypos + self.length] != "O":
                    emyty = True

            if emyty == False:
                for j in range(self.length):
                    self.grid[ship.Xpos][ship.Ypos+j] = Box().CreateShipBlock
                count -= 1
            else:
                continue

    @property
    def printTable(self):
        s = ""
        for i in self.grid:
            a = ""
            for j in i:
                a += "  " + a.join(j) + " |"
            s += a + "\n" + "\n"
        return print(s)

    def Attack(self, Attacked, Nulltable=None):
        self.Attacked = Attacked
        self.Nulltable = Nulltable
        if self.Attacked.name == "enemy":
            while True:
                x = int(input("Введите координату по вертикали: "))
                y = int(input("Введите координату по горизонтали: "))
                if self.Attacked.grid[x][y] == "O":
                    self.Attacked.grid[x][y] = Box().FallShipBlock
                    self.Nulltable.grid[x][y] = Box().FallShipBlock
                    self.Attacked.printTable
                    self.Nulltable.printTable
                    print("Промах")
                    break
                elif self.Attacked.grid[x][y] == Box().CreateShipBlock:
                    self.Attacked.grid[x][y] = Box().DestroyShipBlock
                    self.Nulltable.grid[x][y] = Box().DestroyShipBlock
                    self.Attacked.printTable
                    self.Nulltable.printTable
                    print("Попал")
                    break
                elif self.Attacked.grid[x][y] == Box().DestroyShipBlock:
                    print("Это место подбито")
                    continue
                elif self.Attacked.grid[x][y] == Box().FallShipBlock:
                    print("Сюда уже стреляли")
                    continue
        if self.Attacked.name == "player":
            while True:
                x = random.randint(1, 6)
                y = random.randint(1, 6)
                if self.Attacked.grid[x][y] == "O":
                    self.Attacked.grid[x][y] = Box().FallShipBlock
                    break
                elif self.Attacked.grid[x][y] == Box().CreateShipBlock:
                    self.Attacked.grid[x][y] = Box().DestroyShipBlock
                    break
                elif self.Attacked.grid[x][y] == Box().DestroyShipBlock:
                    continue
                elif self.Attacked.grid[x][y] == Box().FallShipBlock:
                    continue

PlayerTable = Table("player")
PlayerTable.SpawnShip(3,1)
PlayerTable.SpawnShip(2,2)
PlayerTable.SpawnShip(1,4)
PlayerTable.printTable

nullTable = Table("enemy")
nullTable.printTable

EnemyTable = Table("enemy")
EnemyTable.SpawnShip(3,1)
EnemyTable.SpawnShip(2,2)
EnemyTable.SpawnShip(1,4)

while True:
    player = False
    for xp in range(1, len(EnemyTable.grid)):
        for yp in range(1, len(EnemyTable.grid[xp])):
            if EnemyTable.grid[xp][yp] == Box().CreateShipBlock:
                player = True

    if player == True:
        PlayerTable.Attack(EnemyTable, nullTable)
    else:
        print("Ты Выйграл")
        break

    enemy = False
    for xe in range(1, len(PlayerTable.grid)):
        for ye in range(1, len(PlayerTable.grid[xe])):
            if PlayerTable.grid[xe][ye] == Box().CreateShipBlock:
                enemy = True

    if enemy == True:
        EnemyTable.Attack(PlayerTable)
    else:
        print("Ты проиграл")
        break