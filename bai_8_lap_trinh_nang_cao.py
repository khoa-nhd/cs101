class Player():
    x = 0
    y = 0
    role = ""
    name = ""
    isCaught = False
    def __init__(self, name, x, y, role, isCaught):
        self.x = x
        self.y = y
        self.role = role
        self.name = name
        self.isCaught = isCaught
    def move(self, direction, step):
        if direction == "up":
            self.y = self.y - step
        elif direction == "down":
            self.y = self.y + step
        elif direction == "right":
            self.x = self.x + step
        elif direction == "left":
            self.x = self.x - step
def find_remaining(players):
    catcher = players[0]
    for runner in players:
        if runner.role == "runner":
            if catcher.x == runner.x and catcher.y == runner.y:
                runner.isCaught = True
    return players


players = [
        Player('Khoa', 33, 96, 'catcher', False),
	Player('MeNhan', 33, 48, 'runner', False),
	Player('BaCuong', 34, 77, 'runner', False),
	Player('Khoi', 57, 93, 'runner', False)
]
actions = [
        [3, 'up', 2],
	[0, 'right', 24],
	[0, 'up', 5]
]
for action in actions:
    index = action[0]
    players[index].move(action[1], action[2])
    players = find_remaining(players)

remaining_players_name = []
for player in players: 
    if player.role == 'runner' and player.isCaught == False:
        remaining_players_name.append(player.name)
print(remaining_players_name)