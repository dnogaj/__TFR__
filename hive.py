import math
import random
import numpy
from game.game_parameters import GameParameters as gp
import utils

"""
    Hive Module
there you can see a step by step creation of the Tre and decision process 
"""


class Tre:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.strength_path = 10

    """next_step -> for every object (car) in list of objects (cars) we are checking if it collide with any barrier, if so we delete the car's path, if not we perform get_deciosion() function and expand our path data"""

    def next_step(self, cars):
        cars_new = []
        for car in cars:
            if car.colide:
                # print(car.colide)
                self.purge_path(car.path)
            else:
                decision = self.get_decision(car.path.copy())
                car.turn = decision
                # print(decision, car.turn)
                car.path.append(decision)
                # print(car.path)
                cars_new.append(car)
        return cars_new

    def function(self):
        if self.left is None:
            self.left = Tre(1)
        if self.right is None:
            self.right = Tre(1)
        decision = random.choices([-1, 1], [self.left.data, self.right.data], k=1)[0]
        # print(self.left.data)
        # print(self.right.data)
        if decision == -1:
            self.left.data += self.strength_path
        elif decision == 1:
            self.right.data += self.strength_path
        return decision

    def get_decision(self, path):
        # # print(path)
        # try:
        #     next_node = path.pop(0)
        # except:
        #     next_node = 0
        #     print("oops")
        #
        if len(path) == 0:
            return self.function()
        else:
            next_node = path.pop(0)
            if next_node == -1:
                return self.left.get_decision(path)
            elif next_node == 1:
                return self.right.get_decision(path)

    def purge_path(self, path):
        if len(path) == 0:
            self.data -= 1
        else:
            next_node = path.pop(0)
            if next_node == -1:
                self.left.purge_path(path)
                self.data -= self.strength_path
            elif next_node == 1:
                self.right.purge_path(path)
                self.data -= self.strength_path


# tree = Tre(1)
# mypath = []
# # tree.right = Tre(2)
# # tree.left = Tre(2)
# # tree.right.right = Tre(33)
# # tree.right.left = Tre(33)
# # tree.left.right = Tre(3)
# # tree.left.left = Tre(3)
# print(tree.get_decision(mypath))


class Ants:
    def __init__(self, size):
        self.size = []
        self.size.append(utils.position_fix(size[0]))
        self.size.append(utils.position_fix(size[1]))
        print(self.size)
        self.matrix = [[1 for x in range(self.size[0])] for y in range(self.size[1])]
        self.scent_strength = 16
        # print(self.matrix)
        # self.scents_of_death = []

    def decide(self, car_position_x, car_position_y, car_rotation):
        rotation_matrix = [[math.cos(math.radians(car_rotation)), -math.sin(math.radians(car_rotation))],
                           [math.sin(math.radians(car_rotation)), math.cos(math.radians(car_rotation))]]

        left_points = []
        right_points = []
        sens_half_width = 1
        sens_length = 1
        # straight_points = []
        # for y in range(sens_length):
        #     # straight_points.append([0, y + 1])
        #     for x in range(sens_half_width):
        #         # print([-x - 1, y + 1])
        #         # print([x + 1, y + 1])
        #         left_points.append(numpy.matmul([-x - 1, y + 2], rotation_matrix))
        #         right_points.append(numpy.matmul([x + 1, y + 2], rotation_matrix))
        left_points.append([-1, 2])
        right_points.append([1, 2])
        left_points.append([-2, 1])
        right_points.append([2, 1])
        for i in range(len(left_points)):
            left_points[i] = numpy.matmul(left_points[i], rotation_matrix)
            right_points[i] = numpy.matmul(right_points[i], rotation_matrix)
        # left_points.append([-3, 1])
        # right_points.append([3, 1])
        # left_points.append([-1, 1])
        # right_points.append([1, 1])

        # print(len(left_points))
        # print(len(right_points))
        # print(left_points[0])
        # left_points = numpy.multiply(left_points, rotation_matrix)
        # right_points = numpy.multiply(right_points, rotation_matrix)
        for point in range(len(left_points)):
            # print(int(numpy.round(left_points[point][0] + car_position_y, 0)))
            left_points[point] = [int(numpy.round(left_points[point][0] + car_position_x, 0)),
                                  int(numpy.round(left_points[point][1] + car_position_y, 0))]
        for point in range(len(right_points)):
            right_points[point] = [int(numpy.round(right_points[point][0] + car_position_x, 0)),
                                   int(numpy.round(right_points[point][1] + car_position_y, 0))]
        # for point in range(len(straight_points)):
        #     straight_points[point] = [int(numpy.round(straight_points[point][0] + car_position_x, 0)),
        #                               int(numpy.round(straight_points[point][1] + car_position_y, 0))]
        weight_left = 1
        weight_right = 1
        # weight_straight = 1
        for i in range(len(left_points)):
            weight_left += self.matrix[left_points[i][0]][left_points[i][1]]
        for i in range(len(right_points)):
            weight_right += self.matrix[right_points[i][0]][right_points[i][1]]
        # for i in range(len(straight_points)):
        #     weight_straight += self.matrix[straight_points[i][0]][straight_points[i][1]]

        decision = random.choices([-1, 1], [weight_left ** 1, weight_right ** 1], k=1)[0]
        # print(weight_left)
        # print(weight_right)
        # print(decision)
        # print(car_position_x)
        # print(car_position_y)
        # print(left_points)
        # print(right_points)
        return decision

    def next_step(self, cars):
        carsnew = []
        for car in cars:
            if car.colide:
                # print(car.colide)
                max_delete = 50
                for cords in car.scent_of_death:
                    self.matrix[cords[0]][cords[1]] -= self.scent_strength
            else:
                # car.turn = round(random.uniform(-1, 1))
                # car.turn = random.choice([-1, 1])
                car.turn = self.decide(utils.position_fix(car.x_cord), utils.position_fix(car.y_cord), car.angle)
                # car.turn = self.get_decision(car.path)
                # car.path.append(car.turn)
                carsnew.append(car)
                x = utils.position_fix(car.x_cord)
                y = utils.position_fix(car.y_cord)
                car.scent_of_death.append([x, y])
                # print(car.scent_of_death)
                self.matrix[x][y] += self.scent_strength

                if self.matrix[x][y] > 1.2 ** 200:
                    print(":<")
                    for i in range(self.size[0]):
                        for j in range(self.size[1]):
                            if self.matrix[i][j] > 100:
                                self.matrix[i][j] -= 100

        return carsnew

    def show_matrix(self):
        with open('matrix.txt', 'w') as f:
            for row in self.matrix:
                countTmp = 0
                for ttmp in row:
                    countTmp += ttmp
                # print(countTmp)
                f.write(' '.join(str(x) for x in row) + '\n')


# class Ancestors:
#     def __init__(self):
#         self.set_of_sets_all = []
#         self.max_sets = 10
#         self.set_of_sets = []
#         self.base_unfollow_probability = 3 / 4  # always less than 1
#
#     def next_step(self, cars):
#         carsnew = []
#         for car in cars:
#             if car.colide:
#                 self.set_of_sets_all.append(car.path)
#             else:
#                 decision = self.decide(car)
#                 car.turn = decision
#                 car.path.append(decision)
#                 car.jump = car.jump / self.base_unfollow_probability
#                 carsnew.append(car)
#         return carsnew
#
#     def decide(self, car):
#         decision = 0
#         if len(car.path) < len(car.follow_path):
#             #print("carJump", car.jump, " / ", 1 - car.jump)
#             if random.choices([0, 1], [car.jump, 1 - car.jump], k=1)[0]:
#                 decision = car.follow_path[len(car.path)]
#             else:
#                 car.path = car.follow_path
#                 decision = random.choices([-1, 1], [1, 1], k=1)[0]
#         else:
#             decision = random.choices([-1, 1], [1, 1], k=1)[0]
#
#         return decision
#
#     def reduce_sets(self):
#         self.set_of_sets_all = sorted(self.set_of_sets_all, key=len, reverse=True)
#         self.set_of_sets = self.set_of_sets_all[0:self.max_sets].copy()
#         print(len(self.set_of_sets))
#         for i in range(len(self.set_of_sets)):
#             if len(self.set_of_sets[i]) == 0:
#                 self.set_of_sets.pop(i)
#         self.set_of_sets_all = []
#         print("----------------")
#         for tmp_set in self.set_of_sets:
#             print(len(tmp_set))
#         print("================")
#
#     def who_to_follow(self, cars):
#         for car in cars:
#             car.follow_path = random.choice(self.set_of_sets)
#             # car.jump = 1 / len(car.follow_path) / 50
#             car.jump = self.base_unfollow_probability ** len(car.follow_path)
#             # car.jump_old = car.jump

class Ancestors:
    def __init__(self):
        self.set_of_sets_all = []
        self.max_sets = 10
        self.set_of_sets = []
        self.base_unfollow_probability = 1 / 2  # always less than 1

    def next_step(self, cars):
        cars_new = []
        for car in cars:
            if car.colide:
                if car.path:
                    self.set_of_sets_all.append(car.path)
            else:
                self.decide(car)  # sets car turn
                car.path.append(car.turn)
                car.jump = car.jump / self.base_unfollow_probability
                cars_new.append(car)
        return cars_new

    def decide(self, car):
        # decision = 0
        # we decide if we want to abandon righteous path of our ancestors

        if len(car.path) < len(car.follow_path) and car.unfollow_ancestor_path:
            if random.choices([0, 1], [car.jump, 1 - car.jump], k=1)[0]:
                car.turn = car.follow_path[len(car.path)]
            else:
                car.unfollow_ancestor_path = True
                car.turn = random.choice([-1, 1])
        else:
            car.turn = random.choice([-1, 1])

    def reduce_sets(self):
        self.set_of_sets = sorted(self.set_of_sets_all, key=len, reverse=True)[0:self.max_sets].copy()
        self.set_of_sets_all = []

    def who_to_follow(self, cars):
        print("======================")
        for tmp_set in self.set_of_sets:
            print(len(tmp_set), "  ", tmp_set)
        for car in cars:
            car.follow_path = random.choice(self.set_of_sets)
            #car.follow_path = [0]
            car.jump = self.base_unfollow_probability ** len(car.follow_path)
