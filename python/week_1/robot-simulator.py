# Globals for the directions
# Change the values as you see fit
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    def _turn_right(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx + 1) % len(DIRECTIONS)]

    def _turn_left(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx - 1) % len(DIRECTIONS)]

    def _advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        if self.direction == EAST:
            self.x_pos += 1
        if self.direction == SOUTH:
            self.y_pos -= 1
        if self.direction == WEST:
            self.x_pos -= 1

    def move(self, instruction: str):
        for i in instruction:
            if i == 'R':
                self._turn_right()
            if i == 'L':
                self._turn_left()
            if i == 'A':
                self._advance()

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def get_direction(self):
        return self.direction




if __name__ == '__main__':
    robot = Robot(NORTH, 7, 3)
    robot.move('RAALAL')
    print(robot.coordinates)
    print(robot.get_direction())