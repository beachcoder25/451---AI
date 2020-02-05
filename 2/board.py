import random
import numpy as np
import math


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)] # List of lists for board?
        self.fit = 0
        self.optimal_map = np.copy(self.map)
        self.fitness_max = 0
        self.initial_config_list = []
        self.config_list = []
        self.max_config_list = []
        self.temp_config_list = []
        self.step_count = 0
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
        return self.get_config_list()

        

    # Returns a list with the current positions of queens on the board
    def get_config_list(self):

        self.config_list.clear()

        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    self.config_list.append(j)
        return self.config_list

        

     

    # Move Function
    def move(self):
        
        temp = self.get_config_list()
        self.initial_config_list = temp.copy()
        # self.initial_config_list = self.get_config_list()
        
       # print("IC:",self.initial_config_list)
        #print(self.map)
        
        while self.step_count < 100:
            
            for i in range(self.n_queen):

                self.step_count += 1
                if i > 0:
                    self.map = np.copy(self.optimal_map)

                self.map[i] = [0] * self.n_queen # Set current row to all 0's, WORKS
                
                #print("\n\nMOVE FUNCTION\n\n")
                for j in range(self.n_queen):
                    self.map[i][j] = 1 # Flip bit
                    temp_max = self.fitness()
                    #self.show()
                    

                    if temp_max > self.fitness_max:
                        self.fitness_max = temp_max
                        self.save_config()

                        if temp_max == self.nCr(self.n_queen, 2):
                            #print("Max has been reached!!")
                            x = test.get_step_count()
                            print("Optimal fitness value of " + str(test.fitness_max),
                            "has been reached in", x, "steps!!!\n\nWith the following board orientation:\n",self.optimal_map)
                            #print("\n",test.optimal_map)

                            return self.initial_config_list

                    self.map[i][j] = 0 # Flip bit back

                #print("IC:",self.initial_config_list)
        
        if self.step_count == 100:
            print("You have exceeded maximum number of steps:", 100)
            return self.initial_config_list
        
        return self.initial_config_list

    def get_step_count(self):
        return self.step_count


    def calculate_steps(self):

        for i in range(self.n_queen):
            if self.initial_config_list[i] != self.config_list:
                self.step_count += 1

        return self.step_count


    def clear_board(self):
        self.map = [[0 for j in range(self.n_queen)] for i in range(self.n_queen)]

    def nCr(self, n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)
            

class Genetic_algorithm:
   
    def __init__(self, board):
        self.board = board
        self.orientation_lists = [ [] for i in range(self.board.n_queen) ] # Creates list with n empty lists
        self.board_fitness_vals = []
        self.fitness_total = 0
        

    def append_fitness_vals(self):
        print("Ayo")
        self.fitness_total = 0
        self.board_fitness_vals.clear()
        temp_list = []

        for i in range(self.board.n_queen):
            
            self.board.clear_board()
            self.board.set_queens()
            
            fitness_val = self.board.fitness() # Has fitness value
            self.orientation_lists[i].append(self.board.get_config_list()) # Append current config 
            self.board.show()
            #print(self.board.get_config_list())
            #self.orientation_lists.append(this_list.append(temp_list)) 
            temp_list.append(fitness_val)
            self.board_fitness_vals.append(temp_list)
            self.fitness_total += fitness_val

        
        print("F:", self.orientation_lists)
        return self.fitness_total # Sum of lists for division


    





if __name__ == '__main__':
    
    ################
    # Part 1 WORKS
    ################

    test = Board(5)
    test.set_queens()
    temp_list = test.move()
    

    ################
    # End Part 1
    ################


    ################
    # Part 2 INC
    ################

    # board = Board(5)
    # gen_algo = Genetic_algorithm(board)
    # sum = gen_algo.append_fitness_vals()
    # print("Sum:", sum)
    