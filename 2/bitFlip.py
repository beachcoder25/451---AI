def bitFlip(list):

    n = len(list) 
    fitnessMax = 0
    print(n)
    
    for i in range(n):
        if list[i] == 0:
            list[i] == 1
            #max = fitness
            
            if(max > fitnessMax):
                fitnessMax = max




if __name__ == '__main__':
    my_list = [0, 0, 1, 0, 0]
    bitFlip(my_list)