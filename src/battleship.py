
class Battle:
    '''
    SIZE_OF_FIELD = ''
    NUMBER_OF_SHIPS = ''
    TYPES_OF_SHIP = []
    TARGET_PLAYER2 = ''
    TARGET_PLAYER1 = ''
    FIELD1 = []
    FIELD2 = []
    '''

    SIZE_OF_FIELD = '5 E'
    NUMBER_OF_SHIPS = '2'
    TYPES_OF_SHIP = ['Q 1 1 A1 B2', 'P 2 1 D4 C3']
    TARGETS_OF_PLAYER1 = 'A1 B2 B2 B3'
    TARGETS_OF_PLAYER2 = 'A1 B2 B3 A1 D1 E1 D4 D4 D5 D5'
    FIELD1 = []
    FIELD2 = []

    @staticmethod
    def get_input():
        Battle.SIZE_OF_FIELD = input("Please Enter Width (in integer) & Height (in alphabets) of battle field:\n")
        Battle.NUMBER_OF_SHIPS = int(input("Please Enter Number of Ships:\n"))
        Battle.TYPES_OF_SHIP = []
        for _ in range(Battle.NUMBER_OF_SHIPS):
            Battle.TYPES_OF_SHIP.append(input("Enter types, size and co-ordinates of ships:\n"))
        '''
        TARGET_PLAYER2 = input("Player 1: Input target points at battle field of Player 2:\n")
        TARGET_PLAYER1 = input("Player 2: Input target points at battle field of Player 1:\n")
        '''
    @staticmethod
    def pre_process():
        width, height = Battle.SIZE_OF_FIELD.strip().split()
        width = int(width)
        height = int(ord(height)) - 64
        Battle.FIELD1 = [[0 for _ in range(width)] for _ in range(height)]
        Battle.FIELD2 = [[0 for _ in range(width)] for _ in range(height)]
        for ship_details in Battle.TYPES_OF_SHIP:
            category, x, y, cell1, cell2 = ship_details.strip().split()
            x, y = int(x), int(y)
            cell1 = (ord(cell1[0]) - 65, int(cell1[1]) - 1)
            cell2 = (ord(cell2[0]) - 65, int(cell2[1]) - 1)
            # print(cell1, cell2)
            if category == 'P':
                while x > 0:
                    Battle.FIELD1[cell1[0]][cell1[1] + x - 1] = 1
                    Battle.FIELD2[cell2[0]][cell2[1] + x - 1] = 1
                    x -= 1
                while y > 0:
                    Battle.FIELD1[cell1[0] + y - 1][cell1[1]] = 1
                    Battle.FIELD2[cell2[0] + y - 1][cell2[1]] = 1
                    y -= 1

            elif category == 'Q':
                while x > 0:
                    Battle.FIELD1[cell1[0]][cell1[1] + x - 1] = 2
                    Battle.FIELD2[cell2[0]][cell2[1] + x - 1] = 2
                    x -= 1
                while y > 0:
                    Battle.FIELD1[cell1[0] + y - 1][cell1[1]] = 2
                    Battle.FIELD2[cell2[0] + y - 1][cell2[1]] = 2
                    y -= 1

        Battle.TARGETS_OF_PLAYER1 = [(ord(cell[0])-65, int(cell[1])) for cell in
                                     Battle.TARGETS_OF_PLAYER1.strip().split()]
        Battle.TARGETS_OF_PLAYER2 = [(ord(cell[0]) - 65, int(cell[1])) for cell in
                                     Battle.TARGETS_OF_PLAYER2.strip().split()]

        print(Battle.FIELD1)
        print(Battle.FIELD2)

        print(Battle.TARGETS_OF_PLAYER1)
        print(Battle.TARGETS_OF_PLAYER2)

    @staticmethod
    def fire(player, target):
        if player == 1:
            # hit
            if Battle.FIELD2[target[0]][target[1]] > 0:
                Battle.FIELD2[target[0]][target[1]] -= 1
                del Battle.TARGETS_OF_PLAYER1[0]
                return 1
            # miss
            else:
                return 2
        elif player == 2:
            # hit
            if Battle.FIELD1[target[0]][target[1]] > 0:
                Battle.FIELD1[target[0]][target[1]] -= 1
                del Battle.TARGETS_OF_PLAYER2[0]
                return 2
            # miss
            else:
                return 1

    @staticmethod
    def war():
        won = False
        turn_of_player = 1
        while not won:
            if turn_of_player == 1 and len(Battle.TARGETS_OF_PLAYER1) > 0:
                turn_of_player = Battle.fire()
            if turn_of_player == 2:
                turn_of_player = Battle.fire()


# Battle.get_input()
Battle.pre_process()


