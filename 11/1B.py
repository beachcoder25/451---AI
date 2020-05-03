def utility_graph(gamma):

    
    epsilon = 0

    for i in range(99):
        epsilon = epsilon - 1

    # print(epsilon)
    up = (50 * gamma) + epsilon + (10 * gamma)

    print(up)



def main():

    # List of gamma values
    num = 0.50
    gamma_list = []

    for i in range(11):
        num = round(num, 2)
        gamma_list.append(num)
        #print(num)

        num = num + 0.05

    for i in range(len(gamma_list)):
        print(gamma_list[i])

    utility_graph(1)


if __name__ == "__main__":
    main()
