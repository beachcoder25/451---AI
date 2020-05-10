from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import tree, ensemble
from sklearn.ensemble import RandomForestClassifier
import graphviz

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


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


    # def bagging(self):


    def forest(self):

        for i in range(110):
            rf = RandomForestClassifier(n_estimators= i+1)
            rf.fit(self.X_train, self.y_train)
            rf_score = rf.score(self.X_test,self.y_test)

            self.forest_score[i] = rf_score
            print(i, rf_score)

        



    # def boost(self):


    # def summary(self):


if __name__ == '__main__':
    exp = Evaluation()
    exp.decision_tree()
    # exp.bagging()
    exp.forest()
    # exp.boost()
    # exp.summary()