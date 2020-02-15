# Assignment 4 - Airport Location Optimatization

## Description:

The objective function is given by  f(x1,y1,x2,y2,x3,y3)=∑ni=1∑c∈Ci(xi−xc)2+(yi−yc)2  where  n  is the number of the airports and  Ci  is the set of cities whose closest airport is airport  i . The goal of the program is determining the locations of airports that minimize the objective function using gradient based optimizatoin.

The gradient of the objective function is  ∇f(x1,y1,x2,y2,x3,y3)=(2∑c∈C1(x1−xc),2∑c∈C1(y1−yc),2∑c∈C2(x2−xc),2∑c∈C2(y2−yc),2∑c∈C3(x3−xc),2∑c∈C3(y3−yc)) 

By updating  (x1,y1,x2,y2,x3,y3)←(x1,y1,x2,y2,x3,y3)−α∇f(x1,y1,x2,y2,x3,y3)  where  0<α≪1  is a constant, find the optimal locations of the airports  (x1,y1,x2,y2,x3,y3) .

Every time the locations of the airports are updated, plot the objective value as shown in the figure.
