# https://leetcode.com/problems/robot-room-cleaner/
class Robot:
    # returns true if next cell is open and robot moves into the cell.
    # returns false if next cell is obstacle and robot stays on the current cell.
    def move(self):
        pass

    # Robot will stay on the same cell after calling turnLeft/turnRight.
    # Each turn will be 90 degrees.
    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    # Clean the current cell.
    def clean(self):
        pass


class Solution:
    def cleanRoom(self, robot: Robot):
        visited = set()
        # right, down, left, up. Everytime turn right, direction changes to next.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtract(x, y, direction):
            robot.clean()
            visited.add((x, y))

            for i in range(4):
                new_x = x + directions[direction][0]
                new_y = y + directions[direction][1]

                if (new_x, new_y) not in visited and robot.move():
                    backtract(new_x, new_y, direction)
                    go_back(robot)

                robot.turnRight()
                direction = (direction + 1) % 4

        def go_back(robot: Robot):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        backtract(0, 0, 0)
