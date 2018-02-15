class Battle:
    """
    Battle between 2 players.
    """

    def __init__(self):
        self.SIZE_OF_FIELD = ''
        self.NUMBER_OF_SHIPS = ''
        self.TYPES_OF_SHIP = []
        self.TARGETS_OF_PLAYER1 = ''
        self.TARGETS_OF_PLAYER2 = ''
        self.FIELD1 = []
        self.FIELD2 = []

    def get_input(self):
        """
        Take required input from user.

        :return: void
        """
        self.SIZE_OF_FIELD = input(
            "Please Enter Width (in integer) & Height (in alphabets) of battle field:\n"
        )
        self.NUMBER_OF_SHIPS = int(input("Please Enter Number of Ships:\n"))
        self.TYPES_OF_SHIP = []
        for _ in range(self.NUMBER_OF_SHIPS):
            self.TYPES_OF_SHIP.append(
                input("Enter types, size and co-ordinates of ships:\n"))

        self.TARGETS_OF_PLAYER1 = input(
            "Player 1: Input target points at battle field of Player 2:\n")
        self.TARGETS_OF_PLAYER2 = input(
            "Player 2: Input target points at battle field of Player 1:\n")

    def pre_process(self):
        """
        Preprocess the input data.

        :return: void
        """
        width, height = self.SIZE_OF_FIELD.strip().split()
        width = int(width)
        height = int(ord(height)) - 64

        # initialize field cells with 0
        self.FIELD1 = [[0 for _ in range(width)] for _ in range(height)]
        self.FIELD2 = [[0 for _ in range(width)] for _ in range(height)]

        # update field cell values as per the input data
        for ship_details in self.TYPES_OF_SHIP:
            category, x, y, cell1, cell2 = ship_details.strip().split()
            x, y = int(x), int(y)
            cell1 = (ord(cell1[0]) - 65, int(cell1[1]) - 1)
            cell2 = (ord(cell2[0]) - 65, int(cell2[1]) - 1)

            if category == 'P':
                while x > 0:
                    self.FIELD1[cell1[0]][cell1[1] + x - 1] = 1
                    self.FIELD2[cell2[0]][cell2[1] + x - 1] = 1
                    x -= 1
                while y > 0:
                    self.FIELD1[cell1[0] + y - 1][cell1[1]] = 1
                    self.FIELD2[cell2[0] + y - 1][cell2[1]] = 1
                    y -= 1

            elif category == 'Q':
                while x > 0:
                    self.FIELD1[cell1[0]][cell1[1] + x - 1] = 2
                    self.FIELD2[cell2[0]][cell2[1] + x - 1] = 2
                    x -= 1
                while y > 0:
                    self.FIELD1[cell1[0] + y - 1][cell1[1]] = 2
                    self.FIELD2[cell2[0] + y - 1][cell2[1]] = 2
                    y -= 1

        # convert target cells into tuples of (x,y) co-ordinates
        self.TARGETS_OF_PLAYER1 = [
            (ord(cell[0]) - 65, int(cell[1]) - 1)
            for cell in self.TARGETS_OF_PLAYER1.strip().split()
        ]
        self.TARGETS_OF_PLAYER2 = [
            (ord(cell[0]) - 65, int(cell[1]) - 1)
            for cell in self.TARGETS_OF_PLAYER2.strip().split()
        ]

    def fire(self, player, target):
        """
        Fire a missile at target field.

        :param player: player no. (integer)
        :param target: cell coordinates of opposition field (tuple)
        :return: next turn of the player (integer)
        """
        if player == 1:
            # hit
            if self.FIELD2[target[0]][target[1]] > 0:
                self.FIELD2[target[0]][target[1]] -= 1
                print('Player-1 fires a missile with target ' + chr(
                    target[0] + 65) + str(target[1] + 1) + ' which got hit')
                del self.TARGETS_OF_PLAYER1[0]
                return 1
            # miss
            else:
                print('Player-1 fires a missile with target ' + chr(
                    target[0] + 65) + str(target[1] + 1) + ' which got miss')
                del self.TARGETS_OF_PLAYER1[0]
                return 2
        elif player == 2:
            # hit
            if self.FIELD1[target[0]][target[1]] > 0:
                self.FIELD1[target[0]][target[1]] -= 1
                print('Player-2 fires a missile with target ' + chr(
                    target[0] + 65) + str(target[1] + 1) + ' which got hit')
                del self.TARGETS_OF_PLAYER2[0]
                return 2
            # miss
            else:
                print('Player-2 fires a missile with target ' + chr(
                    target[0] + 65) + str(target[1] + 1) + ' which got miss')
                del self.TARGETS_OF_PLAYER2[0]
                return 1

    def war(self):
        """
        Execute war between Player 1 & 2

        :return: 0 (Prints result)
        """
        turn_of_player = 1

        points_1 = 0
        points_2 = 0

        for ship in self.FIELD1:
            points_1 += sum(ship)
        for ship in self.FIELD2:
            points_2 += sum(ship)

        while len(self.TARGETS_OF_PLAYER1) > 0 or len(
                self.TARGETS_OF_PLAYER2) > 0:
            if turn_of_player == 1:
                if len(self.TARGETS_OF_PLAYER1) > 0:
                    turn_of_player = self.fire(1, self.TARGETS_OF_PLAYER1[0])
                    if turn_of_player == 1:
                        points_2 -= 1
                else:
                    print('Player-1 no more missiles left to launch')
                    turn_of_player = 2

            if turn_of_player == 2:
                if len(self.TARGETS_OF_PLAYER2) > 0:
                    turn_of_player = self.fire(2, self.TARGETS_OF_PLAYER2[0])
                    if turn_of_player == 2:
                        points_1 -= 1
                else:
                    print('Player-2 no more missiles left to launch')
                    turn_of_player = 1

            if points_2 == 0:
                print('Player-1 won the battle')
                return 0

            elif points_1 == 0:
                print('Player-2 won the battle')
                return 0

        if len(self.TARGETS_OF_PLAYER2) == 0 and len(
                self.TARGETS_OF_PLAYER1) == 0:
            if points_1 == points_2:
                print('Peace')
                return 0


'''
battle1 = Battle()
battle1.get_input()
battle1.pre_process()
battle1.war()
'''