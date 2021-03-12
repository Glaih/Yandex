class Robot:
    def __init__(self, coordinates):
        self.x, self.y = coordinates
        self.robot_path = [(self.x, self.y)]

    def move(self, waypoints):
        waypoints_list = list(waypoints)
        self.robot_path = [(self.x, self.y)]
        for e in waypoints_list:
            if e == 'N':
                self.y += 1 if self.y < 100 else 0
                if self.robot_path[-1] != (self.x, self.y):
                    self.robot_path.append((self.x, self.y))
            elif e == 'S':
                self.y -= 1 if self.y > 0 else 0
                if self.robot_path[-1] != (self.x, self.y):
                    self.robot_path.append((self.x, self.y))
            elif e == 'W':
                self.x -= 1 if self.x > 0 else 0
                if self.robot_path[-1] != (self.x, self.y):
                    self.robot_path.append((self.x, self.y))
            elif e == 'E':
                self.x += 1 if self.x < 100 else 0
                if self.robot_path[-1] != (self.x, self.y):
                    self.robot_path.append((self.x, self.y))
        return self.x, self.y

    def path(self):
        return self.robot_path


r = Robot((0, 0))
print(r.move('NENW'))
print(*r.path())
print(r.move('WSNE'))
print(*r.path())