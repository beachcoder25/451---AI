import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)] # List of lists for board?
        self.fit = 0
        self.optimal_map = np.copy(self.map)
        self.fitness_max = 0
        self.config_list = []
        self.max_config_list = []
        #print("Board constructed!\n")

    def set_queens(self):
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):
        self.fit = self.n_queen * (self.n_queen - 1) // 2
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit -= 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit -= 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit -= 1
        return self.fit

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ",  self.fit, "\n\n")

    # Iterates through current configuration, and saves positions to a list
    def save_config(self):
        
        self.config_list.clear()
        self.optimal_map = np.copy(self.map) # Make copy of current config 
        ret_list = self.get_config_list()

        return ret_list

    # Returns a list with the current positions of queens on the board
    def get_config_list(self):

        self.config_list.clear()

        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    self.config_list.append(j)
        return self.config_list
        # print("TEMP:",temp_list)
        # print("CONFIG:",self.config_list)
        
        # print("CONFIG:", self.config_list)
        # return temp_list
                    
        # print(self.optimal_map)
        

     

    # Move Function
    def move(self):
        fitness_max = 0
        

        
        for i in range(self.n_queen):
            if i > 0:
                self.map = np.copy(self.optimal_map)

            self.map[i] = [0] * self.n_queen # Set current row to all 0's, WORKS
            
            print("\n\nMOVE FUNCTION\n\n")
            for j in range(self.n_queen):
                self.map[i][j] = 1 # Flip bit
                temp_max = self.fitness()
                self.show()
                

                if temp_max > self.fitness_max:
                    self.fitness_max = temp_max
                    self.max_config_list.clear()
                    #self.max_config_list = self.save_config()
                    print("Huh?")
                    self.save_config()

                self.map[i][j] = 0 # Flip bit back


    def clear_board(self):
        self.map = [[0 for j in range(self.n_queen)] for i in range(self.n_queen)]
        

class Genetic_algorithm:
   
    def __init__(self, board):
        self.board = board
        self.orientation_lists = [ [] for i in range(self.board.n_queen) ] # Creates list with n empty lists
        #print(self.orientation_lists)
        #self.board.show()
        # self.fitness_val = 0
        self.fitness_total = 0
        

    def append_fitness_vals(self):
        print("Ayo")
        self.fitness_total = 0
        for i in range(self.board.n_queen):
            self.board.clear_board()
            self.board.set_queens()
            
            fitness_val = self.board.fitness() # Has fitness value
            self.orientation_lists[i].append(self.board.get_config_list()) # Append current config 
            self.board.show()
            #print(self.board.get_config_list())
            #self.orientation_lists.append(this_list.append(temp_list)) 
            self.fitness_total += fitness_val

        return self.fitness_total # Sum of lists for division


    





if __name__ == '__main__':
    
    ################
    # Part 1 WORKS
    ################

    # test = Board(5)
    # test.set_queens()
    # test.move()
    # print("\nOptimal: " + str(test.fitness_max))
    # print("\nFitness Max config: ", str(test.config_list))
    # print(test.optimal_map)

    ################
    # End Part 1
    ################


    ################
    # Part 2 INC
    ################

    board = Board(5)
    gen_algo = Genetic_algorithm(board)
    sum = gen_algo.append_fitness_vals()
    print("Sum:", sum)
    