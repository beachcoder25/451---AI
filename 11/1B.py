import matplotlib.pyplot as plt

def utility_graph_up(gamma): 
    epsilon_up = 0
    epsilon_down = 0

    for i in range(99):
        epsilon_up = epsilon_up - (gamma**i)
        epsilon_down = epsilon_down + (gamma**i)

    # print(epsilon)
    up = (50 * gamma) + epsilon_up + (10 * (gamma**101))
    down = (-50 * gamma) + epsilon_down + (-10 * (gamma**101))

    return up, down



def main():

    # List of gamma values
    num = 0

    gamma_list = []
    up_list = []
    down_list = []

    # Range 21 to go from 0 - 1 in 0.5 increments
    for i in range(51):
        num = round(num, 2)
       
        gamma_list.append(num)
        #print(num)

        num = num + 0.02

    for i in range(len(gamma_list)):

        up, down = utility_graph_up(gamma_list[i])
        up_list.append(up)
        down_list.append(down)

    # GRAPHING

    plt.plot(gamma_list, up_list, 'r+')
    plt.plot(gamma_list, down_list, 'b+')
    
    plt.axis([0, 1, -50, 50])
    plt.suptitle('Question 1B')
    plt.xlabel('Gamma Value')
    plt.ylabel('Utility Value')
    plt.show()


if __name__ == "__main__":
    main()
