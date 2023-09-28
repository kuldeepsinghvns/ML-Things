from sklearn import tree
import matplotlib.pyplot as plt
import pandas
import sys
from sklearn.tree import DecisionTreeClassifier


def division(n):
    if n==2:
        return "Lose"
    return "Win"

def classification(n):
    if n<Team1:
        return 2
    return 1

Team1=[40,50,37,87,75]
Team2=[37,51,37,67,77]

result=["Win","Lose"]
