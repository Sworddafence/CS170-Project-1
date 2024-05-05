#import random
#from queue import PriorityQueue
from queue import Queue
import time


#def default_initial_state():
#    # Create a list representing the initial state of the puzzle
#    initial_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#    return initial_state


#def input_initial_state():

#    print("Enter the numbers for the initial state of the 8-puzzle:")
#    initial_state = [] #empty state
#    row_num = 1 
#    #user input for each row of the puzzle
#    for _ in range(3):
#        print("Row : " , row_num)
#        row = input("Enter numbers for row separated by spaces: ").strip().split()
#        row_num = row_num + 1
#        initial_state.extend([int(num) for num in row])
#    return initial_state

#def print_puzzle(state):
#    #Print the puzzle grid
#    for i in range(3):
#        print(" ".join(map(str, state[i * 3: (i + 1) * 3])))

class Graph:
    def __init__(self, matrix, blank=None, movesdone=None, generation=None):
        self.matrix = matrix
        self.blank = blank
        self.movesdone = movesdone if movesdone is not None else []
        self.generation = generation if generation is not None else 0

    def print(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))
        print() 

    def can_move_left(self):
        if(self.blank[1] == 0):
            return False
        return True
    
    def can_move_right(self):
        if(self.blank[1] == 2):
            return False
        return True
    def can_move_up(self):
        if(self.blank[0] == 0):
            return False
        return True

    def can_move_down(self):
        if(self.blank[0] == 2):
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
            tempmatrix[self.blank[0]][self.blank[1] -1] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("left")
            tempgraph = Graph(tempmatrix, [self.blank[0], self.blank[1] - 1], movesdone, gen)
            matrixs.append(tempgraph)

        if possible[1]:  
            tempmatrix = [row[:] for row in self.matrix]
            temp = tempmatrix[self.blank[0]][self.blank[1] + 1]
            tempmatrix[self.blank[0]][self.blank[1] + 1] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("right")
            tempgraph = Graph(tempmatrix, [self.blank[0], self.blank[1] + 1], movesdone, gen)
            matrixs.append(tempgraph)

        if possible[2]: 
            tempmatrix = [row[:] for row in self.matrix]
            temp = tempmatrix[self.blank[0] - 1][self.blank[1]]
            tempmatrix[self.blank[0] - 1][self.blank[1]] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("up")
            tempgraph = Graph(tempmatrix, [self.blank[0] - 1, self.blank[1]], movesdone, gen)
            matrixs.append(tempgraph)

        if possible[3]: 
            tempmatrix = [row[:] for row in self.matrix]
            temp = tempmatrix[self.blank[0] + 1][self.blank[1]]
            tempmatrix[self.blank[0] + 1][self.blank[1]] = 0
            tempmatrix[self.blank[0]][self.blank[1]] = temp
            movesdone = self.movesdone[:]
            movesdone.append("down")
            tempgraph = Graph(tempmatrix, [self.blank[0] + 1, self.blank[1]], movesdone, gen)
            matrixs.append(tempgraph)
        return matrixs

    def isdone(self):
        check = [[1,2,3],[4,5,6],[7,8,0]]
        return self.matrix == check


def find_root(bob):
    for index, item in enumerate(bob):
        for jindex, jitem in enumerate(item):
            if(jitem == 0):
                return index, jindex


def uniform_cost():
    #problem_set = [[3,4,1], [2,0,6], [7,8,5]]
    problem_set = [[1,0,3], [4,2,6], [7,5,8]]


    blank = find_root(problem_set)

    first_val = Graph(problem_set, blank)
    UCqueue = Queue()

    UCqueue.put(first_val)
    while not UCqueue.empty():
        node = UCqueue.get()
        time.sleep(0.1)
        node.print()
        if(node.isdone()):
            node.get_moves()
            return node
        else:
            temp = node.do_move()
            for i in temp:
                UCqueue.put(i)
            
    return find_root(problem_set)
# def misplaced():

# def euclidean():



def main():
    uniform_cost()
    ##GUI
    #print("Welcome to the 8 puzzle solver.")
    #select = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle: ")

    #if select == '1':
    #    initial_state = default_initial_state()
    #elif select == '2':
    #    initial_state = input_initial_state()
    #else:
    #    print("Invalid input. Please type '1' or '2'. ")
    #    return

    #print("\nInitial State:")
    #print_puzzle(initial_state)

    #print("\nType '1' for Uniform Cost Search")
    #print("Type '2' for A* with the Misplaced Tile heuristic.")
    #print("Type '3' for A* with the Euclidean distance heuristic.")  

    #algorithm = input("\nEnter your choice of algorithm: ")

    # if algorithm == '1':
    # elif algorithm == '2':
    # elif algorithm == '3':
    # else:
    #     print("Invalid input. Please type '1' or '2' or '3'. ")
    #     return

if __name__ == "__main__":
    main()
