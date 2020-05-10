from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import tree, ensemble
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from mpl_toolkits.mplot3d import Axes3D
import graphviz
import matplotlib.pyplot as plt

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

def isqrt(n):
            x = n
            y = (x + 1) // 2
            while y < x:
                x = y
                y = (x + n // x) // 2
            return x  

class Evaluation:
    def __init__(self):
        self.cancer = load_breast_cancer()
        self.X_train, self.X_test, self.y_train, self.y_test \
        = train_test_split(self.cancer.data, self.cancer.target, test_size=0.2)
        self.tree_score = 0
        self.bagging_score = {}
        self.boost_score = {}
        self.forest_score = {}


    def decision_tree(self):
        clf = tree.DecisionTreeClassifier(criterion="gini")

        # Learn from training dataset
        clf = clf.fit(self.X_train,self.y_train)

        #We built thte tree and trained, now we test
        self.tree_score = clf.score(self.X_test,self.y_test)
        print(self.tree_score)
        dot_data = tree.export_graphviz(clf, out_file=None, feature_names= self.cancer.feature_names)
        graph = graphviz.Source(dot_data)
        graph.render("Cancer")


    def bagging(self):
        for i in range(25):
            bg = BaggingClassifier(tree.DecisionTreeClassifier(), max_samples = 0.5, max_features=1.0, n_estimators=i+1)
            bg.fit(self.X_train, self.y_train)
            bg_score = bg.score(self.X_test,self.y_test)

            self.bagging_score[i] = bg_score
        
        plt.suptitle('Bagging Graph')
        plt.xlabel('n_estimators')
        plt.ylabel('Accuracy %')
        plt.axis([ 0, 24, min(self.bagging_score.values()), max(self.bagging_score.values())])
        plt.plot(*zip(*sorted(self.bagging_score.items())))
        plt.show()


    def forest(self):

        counter = 0 
        for i in range(1, isqrt(30)+1):
            for j in range(1,25):
                clf = ensemble.RandomForestClassifier(n_estimators = j, max_features = i)
                clf= clf.fit(self.X_train, self.y_train)
                self.forest_score[counter] =j, i, clf.score(self.X_test, self.y_test)
                counter+=1 
            
        diListF = sorted(self.forest_score.items()) #sort based on counter value
        #print(diListF)
        c,xyz = zip(*diListF) #seperate counter from rest
        x, y, z = zip(*xyz)   #seperate rest into x,y,z format
        #print( x, y, z)
        
        #plotting the figure

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_title ('RandomForest classification scores')
        ax.set_xlabel('n_estimators')
        ax.set_ylabel('max_feature')
        ax.set_zlabel('Score')
        ax.set_xlim(1, 25)
        ax.set_ylim(1, 5)
        ax.set_zlim(.80,.99 )
        ax.grid(True)
        ax.plot(x,y,z)
        ax.scatter(x,y,z)
        plt.show()

    def boost(self):
        for i in range(25):
            bg = AdaBoostClassifier(tree.DecisionTreeClassifier(), n_estimators=i+1, learning_rate=1)
            bg.fit(self.X_train, self.y_train)
            bg_score = bg.score(self.X_test,self.y_test)

            self.boost_score[i] = bg_score
        
        plt.suptitle('Boost Graph')
        plt.xlabel('n_estimators')
        plt.ylabel('Accuracy %')
        plt.axis([ 0, 24, min(self.boost_score.values()), max(self.boost_score.values())])
        plt.plot(*zip(*sorted(self.boost_score.items())))
        plt.show()


    # def summary(self):


if __name__ == '__main__':
    exp = Evaluation()
    exp.decision_tree()
    exp.bagging()
    exp.forest()
    exp.boost()
    # exp.summary()