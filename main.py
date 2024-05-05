import random
from queue import PriorityQueue

def default_initial_state():
    # Create a list representing the initial state of the puzzle
    initial_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return initial_state


def input_initial_state():

    print("Enter the numbers for the initial state of the 8-puzzle:")
    initial_state = [] #empty state
    row_num = 1 
    #user input for each row of the puzzle
    for _ in range(3):
        print("Row : " , row_num)
        row = input("Enter numbers for row separated by spaces: ").strip().split()
        row_num = row_num + 1
        initial_state.extend([int(num) for num in row])
    return initial_state

def print_puzzle(state):
    #Print the puzzle grid
    for i in range(3):
        print(" ".join(map(str, state[i * 3: (i + 1) * 3])))


# def uniform_cost():

# def misplaced():

# def euclidean():



def main():
    #GUI
    print("Welcome to the 8 puzzle solver.")
    select = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle: ")

    if select == '1':
        initial_state = default_initial_state()
    elif select == '2':
        initial_state = input_initial_state()
    else:
        print("Invalid input. Please type '1' or '2'. ")
        return

    print("\nInitial State:")
    print_puzzle(initial_state)

    print("\nType '1' for Uniform Cost Search")
    print("Type '2' for A* with the Misplaced Tile heuristic.")
    print("Type '3' for A* with the Euclidean distance heuristic.")  

    algorithm = input("\nEnter your choice of algorithm: ")

    # if algorithm == '1':
    # elif algorithm == '2':
    # elif algorithm == '3':
    # else:
    #     print("Invalid input. Please type '1' or '2' or '3'. ")
    #     return

if __name__ == "__main__":
    main()
