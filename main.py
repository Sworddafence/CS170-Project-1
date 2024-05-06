# import random
# from queue import PriorityQueue
from queue import Queue
import time
import heapq
import math



def default_initial_state():
    # Create a list representing the initial state of the puzzle
    initial_state = [[1, 2, 4], [0, 5, 3], [7, 8, 6]]
    return initial_state



def input_initial_state():

    print("Enter the numbers for the initial state of the 8-puzzle:")
    initial_state = []  # empty state
    row_num = 1
    # user input for each row of the puzzle
    for _ in range(3):
        print("Row : ", row_num)
        row = input(
            "Enter numbers for row separated by spaces: ").strip().split()
        row_num = row_num + 1
        initial_state.append([int(num) for num in row])
    return initial_state



def print_puzzle(state):
    # Print the puzzle grid
    for row in state:
        print(" ".join(map(str, row)))


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def empty(self):
        return len(self._queue) == 0

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def empty(self):
        return len(self._queue) == 0

class Graph:
    def __init__(self, matrix, blank=None, movesdone=None, generation=None):
        self.matrix = matrix
        self.blank = blank
        self.movesdone = movesdone if movesdone is not None else []
        self.generation = generation if generation is not None else 0

    def print_state(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))
        print()

    def can_move_left(self):
        if (self.blank[1] == 0):
            return False
        return True

    def can_move_right(self):
        if (self.blank[1] == 2):
            return False
        return True

    def can_move_up(self):
        if (self.blank[0] == 0):
            return False
        return True

    def can_move_down(self):
        if (self.blank[0] == 2):
            return False
        return True

    def can_move(self):
        moves = []
        moves.append(1 if self.can_move_left() else 0)
        moves.append(1 if self.can_move_right() else 0)
        moves.append(1 if self.can_move_up() else 0)
        moves.append(1 if self.can_move_down() else 0)
        return moves

    def get_moves(self):
        print(self.movesdone)

    def do_move(self):
        matrixs = []
        possible = self.can_move()
        gen = self.generation + 1
        if possible[0]:
            tempmatrix = [row[:] for row in self.matrix]
            temp = self.matrix[self.blank[0]][self.blank[1]-1]
            tempmatrix[self.blank[0]][self.blank[1] - 1] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("left")
            tempgraph = Graph(
                tempmatrix, [self.blank[0], self.blank[1] - 1], movesdone, gen)
            matrixs.append(tempgraph)

        if possible[1]:
            tempmatrix = [row[:] for row in self.matrix]
            temp = tempmatrix[self.blank[0]][self.blank[1] + 1]
            tempmatrix[self.blank[0]][self.blank[1] + 1] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("right")
            tempgraph = Graph(
                tempmatrix, [self.blank[0], self.blank[1] + 1], movesdone, gen)
            matrixs.append(tempgraph)

        if possible[2]:
            tempmatrix = [row[:] for row in self.matrix]
            temp = tempmatrix[self.blank[0] - 1][self.blank[1]]
            tempmatrix[self.blank[0] - 1][self.blank[1]] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("up")
            tempgraph = Graph(
                tempmatrix, [self.blank[0] - 1, self.blank[1]], movesdone, gen)
            matrixs.append(tempgraph)

        if possible[3]:
            tempmatrix = [row[:] for row in self.matrix]
            temp = tempmatrix[self.blank[0] + 1][self.blank[1]]
            tempmatrix[self.blank[0] + 1][self.blank[1]] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("down")
            tempgraph = Graph(
                tempmatrix, [self.blank[0] + 1, self.blank[1]], movesdone, gen)
            matrixs.append(tempgraph)
        return matrixs

    def isdone(self):
        check = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.matrix == check


def find_root(bob):
    for index, item in enumerate(bob):
        for jindex, jitem in enumerate(item):
            if (jitem == 0):
                return index, jindex


def uniform_cost(initial_state):
    nodes_expanded = 0
    queue_size = 1 
    hash_table = {}
    blank = find_root(initial_state)
    first_val = Graph(initial_state, blank)
    UCqueue = Queue()
    UCqueue.put(first_val)
    hash_table[tuple(map(tuple, first_val.matrix))] = True
    while not UCqueue.empty():
        queue_size-=1 
        node = UCqueue.get()
        hash_table[tuple(map(tuple, node.matrix))] = True
        node.print_state()
        if (node.isdone()):
            node.get_moves()
            print(f"To solve this problem the search algorithm expanded a total of {nodes_expanded} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {queue_size+1}.")
            print(f"The depth of the goal node was {node.generation}.")
            return node
        else:
            temp = node.do_move()
            nodes_expanded+=1 
            print("Best State to expand with g(n) = " + str(node.generation))
            for i in temp:
                if not tuple(map(tuple, i.matrix)) in hash_table:
                    UCqueue.put(i)
                    queue_size+=1

    return find_root(initial_state)


def misplaced_tiles(current_matrix):

    num_misplaced = 0
    goal_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    n = len(goal_matrix)

    for i in range(n):
        for j in range(n):
            if goal_matrix[i][j] != 0 and goal_matrix[i][j] != current_matrix[i][j]:
                num_misplaced += 1

    return num_misplaced


def misplaced(initial_state):
    nodes_expanded = 0
    queue_size = 1
    blank = find_root(initial_state)
    hash_table = {}
    first_val = Graph(initial_state, blank)
    MPqueue = PriorityQueue()
    MPqueue.push(first_val, misplaced_tiles(
        first_val.matrix) + first_val.generation)
    hash_table[tuple(map(tuple, first_val.matrix))] = True

    while not MPqueue.empty():

        node = MPqueue.pop()
        queue_size -= 1
        node.print_state()
        hash_table[tuple(map(tuple, node.matrix))] = True
        if (node.isdone()):
            node.get_moves()
            print(f"To solve this problem the search algorithm expanded a total of {nodes_expanded} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {queue_size+1}.")
            print(f"The depth of the goal node was {node.generation}.")
            return node
        else:
            temp = node.do_move()
            nodes_expanded+=1
            
            print("Best State to expand with g(n) = " + str(node.generation) +
                  " h(n) = " + str(misplaced_tiles(node.matrix)))
            for i in temp:
                if not tuple(map(tuple, i.matrix)) in hash_table:
                    MPqueue.push(i, misplaced_tiles(i.matrix) + i.generation)
                    queue_size+=1

    return find_root(initial_state)



def euclidean_distance(curr):
    def find_position(matrix, value):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == value:
                    return (i, j)
        return None
    distance = 0
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    for i in range(len(curr)):
        for j in range(len(curr[0])):
            value = curr[i][j]
            if value != 0:
                goal_pos = find_position(goal, value)
                distance += math.sqrt((i - goal_pos[0])
                                      ** 2 + (j - goal_pos[1]) ** 2)
    return distance


def euclidean(initial_state):
    nodes_expanded = 0
    queue_size = 1

    blank = find_root(initial_state)
    first_val = Graph(initial_state, blank)
    hash_table = {}
    Equeue = PriorityQueue()
    Equeue.push(first_val, euclidean_distance(
        first_val.matrix) + first_val.generation)
    hash_table[tuple(map(tuple, first_val.matrix))] = True
    while not Equeue.empty():
        queue_size -=1
        node = Equeue.pop()
        node.print_state()
        hash_table[tuple(map(tuple, node.matrix))] = True
        if (node.isdone()):
            node.get_moves()
            print(f"To solve this problem the search algorithm expanded a total of {nodes_expanded} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {queue_size+1}.")
            print(f"The depth of the goal node was {node.generation}.")
            return node
        else:
            nodes_expanded+=1
            temp = node.do_move()
            print("Best State to expand with g(n) = " + str(node.generation) +
                  " h(n) = " + str(euclidean_distance(node.matrix)))
            for i in temp:
                if not tuple(map(tuple, i.matrix)) in hash_table:
                    Equeue.push(i, euclidean_distance(
                        i.matrix) + i.generation)
                    queue_size+=1

    return find_root(initial_state)


    
def main():
    # interface
    print("Welcome to the 8 puzzle solver.")
    while True:
        select = input(
            "Type '1' to use a default puzzle, or '2' to enter your own puzzle: ")
        if select == '1':
            initial_state = default_initial_state()
        elif select == '2':
            initial_state = input_initial_state()
        else:
            print("Invalid input. Please type '1' or '2'. ")
            continue  # repeats interface

        print("\nInitial State:")
        print_puzzle(initial_state)

        print("\nType '1' for Uniform Cost Search")
        print("Type '2' for A* with the Misplaced Tile heuristic.")
        print("Type '3' for A* with the Euclidean distance heuristic.")

        while True:
            algorithm = input("\nEnter your choice of algorithm: ")
            if algorithm == '1':
                uniform_cost(initial_state)
                break
            elif algorithm == '2':
                misplaced(initial_state)
                break
            elif algorithm == '3':
                euclidean(initial_state)
                break
            else:
                print("Invalid input. Please type '1' or '2' or '3'. ")
                continue  # repeats interface
        continue_search = input(
            "\nDo you want to continue with another initial state? Type 'y' for yes and 'n' for no: ")
        if continue_search not in ['y', 'yes']:
            break


if __name__ == "__main__":
    main()
