# MAZE PROGRAMME

"""Solving a maze problem using artificial intelligence"""


def actions(state):
    row, column = state
    moves = [(row, column - 1), (row, column + 1), (row - 1, column),
             (row + 1, column)]
    available_moves = [move for move in moves if
                       move not in maze.wall_cordinates and
                       move[0] in range(maze.height) and move[1] in
                       range(maze.width) and move not in Node.explored_state]
    return available_moves


class Node:
    frontier = []
    explored_state = []
    path = []
    total_path = []

    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action
        self.frontier.insert(0, self.state)

        while True:

            if self.frontier is []:
                print("There is no solution")
            elif self.state == maze.goal:
                break

            self.action = actions(self.frontier[0])
            self.path.append(self.state)
            self.total_path.append(self.state)
            self.explored_state.append(self.state)

            if len(self.action) != 0:
                for value in self.action:
                    self.frontier.insert(0, value)
                self.parent = self.state
                self.frontier.remove(self.parent)
            else:
                self.frontier.remove(self.state)
                path = list(reversed(self.path))

                for i in path:
                    if len(actions(i)) == 0:
                        self.path.remove(i)
                    else:
                        break

            self.state = self.frontier[0]


class Maze:

    def __init__(self, file_name):
        self.file = file_name
        self.path = []

        with open(self.file) as f:
            self.contents = f.read()
        self.contents = self.contents.splitlines()

        self.height = len(self.contents)
        self.width = max([len(line) for line in self.contents])

        self.start = None
        self.goal = None
        self.wall = None
        self.wall_cordinates = []

    def walls(self):

        self.wall = []
        for i in range(self.height):
            row = []
            for j in range(self.width):

                try:
                    if self.contents[i][j] == 'A':
                        self.start = (i, j)
                        row.append(False)
                    elif self.contents[i][j] == 'B':
                        self.goal = (i, j)
                        row.append(False)
                    elif self.contents[i][j] == ' ':
                        row.append(False)
                    else:
                        row.append(True)
                        self.wall_cordinates.append((i, j))

                except IndexError:
                    row.append(False)
            self.wall.append(row)

    def print_wall(self):

        # print(self.contents)

        for i, row in enumerate(self.wall):
            for j, column in enumerate(row):

                if column:
                    print('█', end='')
                elif (i, j) == self.start:
                    print('A', end='')
                elif (i, j) == self.goal:
                    print('B', end='')
                else:
                    if (i, j) in Node.path:
                        print('*', end='')
                    elif (i, j) in Node.total_path:
                        print('-', end='')
                    else:
                        print(' ', end='')
            print()

        Node(state=self.start, parent=None, action=None)


if __name__ == '__main__':
    maze = Maze('maze.txt')
    maze.walls()
    maze.print_wall()
    print()
    maze.print_wall()
