import math
from random import *

from WebotsSim.libraries.RobotLib.MazeAndPcsParcer import parse_maze


class Maze:
    def __init__(self, maze_file):

        self.length = 0
        self.width = 0
        self.boundary_walls = []
        self.starting_location = []
        self.goal_locations = []
        self.obstacles = []
        self.landmarks = []

        walls, goals, start_positions, landmarks = parse_maze(maze_file)

        for index, row in walls.iterrows():
            if index <= 3:
                self.boundary_walls.append(BoundaryWall(row['x1'], row['y1'], row['x2'], row['y2'], id=index))
            else:
                self.obstacles.append(Obstacle(row['x1'], row['y1'], row['x2'], row['y2'], id=index - 4))

        for index, row in start_positions.iterrows():
            self.starting_location.append(StartingPosition(row['x'], row['y'], row['theta']))

        for index, row in goals.iterrows():
            self.goal_locations.append(Goal(row['x'], row['y'], row['id']))

        for index, row in landmarks.iterrows():
            self.landmarks.append(Landmark(row['x'], row['y'], height=row['height'] ,color=[row['red'], row['green'], row['blue']], id=index))

    # Returns random starting positions
    def get_random_starting_position(self):
        return sample(self.starting_location, 1)[0]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self, robot_position):
        return math.dist((self.x, self.y), (robot_position[0], robot_position[1])) - robot_position[2]


class Goal(Point):
    def __init__(self, x, y, id):
        super().__init__(x, y)
        self.goal_id = id


class StartingPosition(Point):
    def __init__(self, x, y,theta):
        super().__init__(x, y)
        self.theta =theta


class BoundaryWall:
    def __init__(self, x1, y1, x2, y2, height=0.5, width=0.012, id=0):
        self.end_point1 = Point(x1, y1)
        self.end_point2 = Point(x2, y2)
        self.height = height
        self.width = width
        self.length = math.dist((x1, y1), (x2, y2))
        self.id = id
        self.center_mass = Point((self.end_point1.x + self.end_point2.x) / 2,
                                 (self.end_point1.y + self.end_point2.y) / 2)
        self.dimensions = [self.width, self.length, self.height]
        self.translation = [(self.end_point1.x + self.end_point2.x) / 2,
                            (self.end_point1.y + self.end_point2.y) / 2,
                            self.height / 2]
        theta = math.atan2(self.end_point1.x - self.end_point2.x, self.end_point1.y - self.end_point2.y)
        self.rotation = [0, 0, 1, theta]

    def get_webots_translation_string(self):
        txt = 'translation {x:.2f} {y:.2f} {z:.2f}'
        return txt.format(x=self.translation[0], y=self.translation[1], z=self.translation[2])

    def get_webots_rotation_string(self):
        txt = 'rotation {x:.2f} {y:.2f} {z:.2f} {theta:.2f}'
        return txt.format(x=self.rotation[0], y=self.rotation[1], z=self.rotation[2], theta=self.rotation[3])

    def get_webots_size_string(self):
        txt = 'size {width:.2f} {length:.2f} {height:.2f}'
        return txt.format(width=self.width, length=self.length, height=self.height)

    def get_webots_node_string(self):
        node_string = "{translation} {rotation} {size}".format(translation=self.get_webots_translation_string(),
                                                               rotation=self.get_webots_rotation_string(),
                                                               size=self.get_webots_size_string())
        return 'DEF Boundary_Wall{id} Obstacle '.format(id=self.id) + '{ ' + node_string + ' }'


class Obstacle:
    def __init__(self, x1, y1, x2, y2, height=0.5, width=0.012, id=0):
        self.end_point1 = Point(x1, y1)
        self.end_point2 = Point(x2, y2)
        self.height = height
        self.width = width
        self.length = math.dist((x1, y1), (x2, y2))
        self.id = id
        self.center_mass = Point((self.end_point1.x + self.end_point2.x) / 2,
                                 (self.end_point1.y + self.end_point2.y) / 2)
        self.dimensions = [self.width, self.length, self.height]
        self.translation = [(self.end_point1.x + self.end_point2.x) / 2,
                            (self.end_point1.y + self.end_point2.y) / 2,
                            self.height / 2]
        theta = math.atan2(self.end_point1.x - self.end_point2.x, self.end_point1.y - self.end_point2.y)
        self.rotation = [0, 0, 1, theta]

    def get_webots_translation_string(self):
        txt = 'translation {x:.2f} {y:.2f} {z:.2f}'
        return txt.format(x=self.translation[0], y=self.translation[1], z=self.translation[2])

    def get_webots_rotation_string(self):
        txt = 'rotation {x:.2f} {y:.2f} {z:.2f} {theta:.2f}'
        return txt.format(x=self.rotation[0], y=self.rotation[1], z=self.rotation[2], theta=self.rotation[3])

    def get_webots_size_string(self):
        txt = 'size {width:.2f} {length:.2f} {height:.2f}'
        return txt.format(width=self.width, length=self.length, height=self.height)

    def get_webots_node_string(self):
        node_string = "{translation} {rotation} {size}".format(translation=self.get_webots_translation_string(),
                                                               rotation=self.get_webots_rotation_string(),
                                                               size=self.get_webots_size_string())
        return 'DEF Obstacle_{id} Obstacle '.format(id=self.id) + '{ ' + node_string + ' }'


class Landmark:
    def __init__(self, x, y, height=1.5, radius=.25, color=[1, 1, 1], id=0):
        self.height = height
        self.radius = radius
        self.x = x
        self.y = y
        self.z = height/2
        self.translation = [x, y, self.z]
        self.id = id
        self.color = color

    def get_webots_translation_string(self):
        txt = 'translation {x:.2f} {y:.2f} {z:.2f}'
        return txt.format(x=self.translation[0], y=self.translation[1], z=self.translation[2])

    def get_webots_size_string(self):
        txt = 'size {width:.2f} {length:.2f} {height:.2f}'
        return txt.format(width=self.height, length=self.radius, height=self.radius-.01)

    def get_webots_color_string(self):
        txt = 'color {red:.2f} {green:.2f} {blue:.2f}'
        return txt.format(red=self.color[0], green=self.color[1], blue=self.color[2])

    def get_webots_node_string(self):
        node_string = "{translation} {color} {size}".format(translation=self.get_webots_translation_string(),
                                                            color=self.get_webots_color_string(),
                                                            size=self.get_webots_size_string())
        return 'DEF Landmark_{id} Landmark '.format(id=self.id) + '{ ' + node_string + ' }'
