import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)] # List of lists for board?
        self.fit = 0
        self.optimal_map = np.copy(self.map)
        self.fitness_max = 0
        print("Board constructed!\n")

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
        
        config_list = []
        self.optimal_map = np.copy(self.map) # Make copy of current config 

        for i in range(self.n_queen):
            for j in range(self.n_queen):

                if self.map[i][j] == 1:
                    
                    config_list.append(j)
                    
        # print(self.optimal_map)
        # print("\nFitness Max config: ", str(config_list))

    

    # Move Function
    def move(self):
        fitness_max = 0
        

        
        for i in range(1):
            self.map[i] = [0] * self.n_queen # Set current row to all 0's, WORKS
            
            print("\n\nMOVE FUNCTION\n\n")
            for j in range(self.n_queen):
                self.map[i][j] = 1 # Flip bit
                temp_max = self.fitness()
                self.show()
                

                if temp_max > self.fitness_max:
                    self.fitness_max = temp_max
                    self.save_config()

                self.map[i][j] = 0 # Flip bit back
        
        print("\n\nFitness max: " + str(fitness_max))
        
                    
                    
                
                #else if self.map[i][j] == 0:




        
if __name__ == '__main__':
    test = Board(5)
    test.set_queens()
    # test.fitness()
    # test.show()
    test.move()
    print("\nOptimal: " + str(test.fitness_max))
    print(test.optimal_map)