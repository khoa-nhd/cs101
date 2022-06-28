class Player:
    x = 0
    y = 0
    name = ""
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def move(self, direction, step):
        if direction == "up":
            self.y = self.y - step
        elif direction == "down":
            self.y = self.y + step
        elif direction == "right":
            self.x = self.x + step
        elif direction == "left":
            self.x = self.x - step
            
            
players = [
        Player('Khoa', 97, 61),
	Player('Khoi', 68, 8),
	Player('BaCuong', 33, 83),
	Player('MeNhan', 73, 94),
	Player('MeoBi', 66, 98)
]
actions = [
        [1, 'down', 3],
	[1, 'left', 1],
	[3, 'left', 5],
	[4, 'left', 4],
	[0, 'down', 3],
	[3, 'down', 6],
	[1, 'down', 8],
	[0, 'down', 9]
]
for action in actions:
    index = action[0]
    players[index].move(action[1], action[2])
    print(players[index].x, players[index].y)