import matplotlib.pyplot as plt

def utility_graph_up(gamma): 
    epsilon = 0

    for i in range(99):
        epsilon = epsilon - (gamma**i)

    # print(epsilon)
    up = (50 * gamma) + epsilon + (10 * (gamma**101))

    print(up)
    return up


def utility_graph_down(gamma):
    epsilon = 0

    for i in range(99):
        epsilon = epsilon + (gamma**i)

    # print(epsilon)
    down = (50 * gamma) + epsilon + (10 * (gamma**101))

    print(down)
    return down


def main():

    # List of gamma values
    num = 0

    gamma_list = []
    up_list = []
    down_list = []

    # Range 21 to go from 0 - 1 in 0.5 increments
    for i in range(101):
        num = round(num, 2)
       
        gamma_list.append(num)
        #print(num)

        num = num + 0.01

    for i in range(len(gamma_list)):
        up_list.append(utility_graph_up(gamma_list[i]))
        down_list.append(utility_graph_down(gamma_list[i]))

    # GRAPHING

    plt.plot(gamma_list, up_list, 'r+')
    plt.plot(gamma_list, down_list, 'b+')
    
    plt.axis([0, 1, -1, 70])
    plt.show()


if __name__ == "__main__":
    main()
