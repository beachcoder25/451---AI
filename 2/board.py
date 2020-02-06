import random
import numpy as np
import math
import random
from random import randint



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
                            x = self.get_step_count()
                            print("Optimal fitness value of " + str(self.fitness_max),
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
        self.orientation_lists = [] # Creates list with n empty lists
        self.board_fitness_vals = []
        self.probability_list = []
        self.selection_list = []
        self.crossover_list = []
        self.sorted_list = []
        self.fitness_total = 0
        

    def append_fitness_vals(self):
        print("Ayo")
        #self.fitness_total = 0
        self.board_fitness_vals.clear()
        temp_list = []
        temp_list_fitness = []

        for i in range(self.board.n_queen):
            
            self.board.clear_board()
            self.board.set_queens()
            
            fitness_val = self.board.fitness() # Has fitness value
            temp_list = self.board.get_config_list()
            self.orientation_lists.append(temp_list.copy()) # Append current config 
            #print("Iteration:",i+1,"with configuration", self.board.get_config_list()) # KEEP THIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            

            #self.board.show()


            #print(self.board.get_config_list())
            #self.orientation_lists.append(this_list.append(temp_list)) 
            temp_list_fitness.append(fitness_val)
            self.board_fitness_vals = temp_list_fitness.copy()
            self.fitness_total += fitness_val

        
        print("Orientation lists:", self.orientation_lists)
        print("Fitness values:", self.board_fitness_vals,"\n")
        self.calculate_probability() # WORKS!!!
        self.sort_by_probability()
        return self.fitness_total # Sum of lists for division

    # Calculate probabilities for each orientation
    def calculate_probability(self):

        for val in self.board_fitness_vals:
            
            temp = float("{0:.2f}".format(val / self.fitness_total))
            #print("val:", val,"Probability:", temp)
            self.probability_list.append(temp)
            #print(temp)
            #print(self.probability_list, "\n")
            #print("Probability:", "{0:.2f}".format(val / self.fitness_total))
    
    # Sorts in ascending order (0.09. 0.18, 0.55, ....)
    def sort_by_probability(self):
        # https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list

        self.orientation_lists = np.array(self.orientation_lists)
        self.probability_list = np.array(self.probability_list)
        inds = self.probability_list.argsort()
        self.sorted_list = self.orientation_lists[inds].tolist()
        print(self.sorted_list)
        

    def selection(self):
        
        
        temp_list = self.probability_list.tolist()
        
        temp_list2 = temp_list.copy()
        print("sum",sum(temp_list2[0:2]))
        probability_sum = 0
        print(temp_list)

        #self.sorted_list.tolist()

        for i in range(8):
            random_num = random.uniform(0, 1)
            #random_num = sum(temp_list2[0:8]) - .0001
            #print(random_num, "<",sum(temp_list2[0:8]))

            if random_num < temp_list2[0]:
                probability_sum += temp_list2[0]
                #print(self.sorted_list)
                self.selection_list.append(self.sorted_list[0])
                #print("p_sum", probability_sum)

            elif random_num > temp_list2[0] and random_num < sum(temp_list2[0:2]):
                
                self.selection_list.append(self.sorted_list[1])
                #print(self.selection_list)
                #print("p_sum", probability_sum)

            elif random_num > sum(temp_list2[0:2]) and random_num < sum(temp_list2[0:3]):

                self.selection_list.append(self.sorted_list[2])
                #print(self.selection_list)

            elif random_num > sum(temp_list2[0:3]) and random_num < sum(temp_list2[0:4]):

                self.selection_list.append(self.sorted_list[3])
                #print(self.selection_list)

            elif random_num > sum(temp_list2[0:4]) and random_num < sum(temp_list2[0:5]):

                self.selection_list.append(self.sorted_list[4])
                #print(self.selection_list)

            elif random_num > sum(temp_list2[0:5]) and random_num < sum(temp_list2[0:6]):

                self.selection_list.append(self.sorted_list[5])
                #print(self.selection_list)

            elif random_num > sum(temp_list2[0:6]) and random_num < sum(temp_list2[0:7]):

                self.selection_list.append(self.sorted_list[6])
                #print(self.selection_list)
            
            elif random_num > sum(temp_list2[0:7]) and random_num <= 1:

                self.selection_list.append(self.sorted_list[7])
                #print(self.selection_list)
            

        print(self.selection_list)
        #print(random_num)

    def crossover(self):

        value = randint(0, 7)

        #self.selection_list.tolist()
        print("RandVal:",value)

        print("Before:",self.selection_list)
        print("Type",type(self.selection_list))



        temp_list0 = self.selection_list[0][:value] + self.selection_list[1][value:]
        temp_list1 = self.selection_list[1][:value] + self.selection_list[0][value:]
        

        self.selection_list[0] = temp_list0
        self.selection_list[1] = temp_list1


        value = randint(0, 7)

        temp_list2 = self.selection_list[2][:value] + self.selection_list[3][value:]
        temp_list3 = self.selection_list[3][:value] + self.selection_list[2][value:]
        

        self.selection_list[2] = temp_list2
        self.selection_list[3] = temp_list3


        value = randint(0, 7)

        temp_list4 = self.selection_list[4][:value] + self.selection_list[5][value:]
        temp_list5 = self.selection_list[5][:value] + self.selection_list[4][value:]
        self.selection_list[4] = temp_list4
        self.selection_list[5] = temp_list5


        value = randint(0, 7)

        temp_list6 = self.selection_list[6][:value] + self.selection_list[7][value:]
        temp_list7 = self.selection_list[7][:value] + self.selection_list[6][value:]
        self.selection_list[6] = temp_list6
        self.selection_list[7] = temp_list7



        print("After:",self.selection_list)




if __name__ == '__main__':
    
    ################
    # Part 1 WORKS
    ################

    # test = Board(5)
    # test.set_queens()
    # temp_list = test.move()
    

    ################
    # End Part 1
    ################


    ################
    # Part 2 INC
    ################

    board = Board(8)
    gen_algo = Genetic_algorithm(board)
    sum1 = gen_algo.append_fitness_vals()
    print("Sum:", sum1)
    gen_algo.selection()
    gen_algo.crossover()
    