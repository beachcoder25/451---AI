# https://towardsdatascience.com/how-to-build-a-market-simulator-using-markov-chains-and-python-7923256f8d29


a_val,b_val,c_val = [],[],[]
# initial state
init_state = np.array([188969, 81356, 14210])
# transition matrix
a = np.array([[ 0.89, 0.75 ,0.49], [ 0.10, 0.22 ,0.44], [ 0.01, 0.03 ,0.07]])
for x in range(10):
    a_val.append(init_state[0])
    b_val.append(init_state[1])
    c_val.append(init_state[2])
    b = init_state
    init_state = a.dot(b)