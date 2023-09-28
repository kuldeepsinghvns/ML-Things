import time
import pandas as pd
from selenium import webdriver
from sklearn import tree
import matplotlib.pyplot as plt

def readExcel():
    df =pd.read_csv('student.csv')
    input_data=df['input_data']
    return input_data

def devision(n):
    if n==2:
        return "false"
    return "true"
def classification(n):

    if n<51:
        return 2
    return 1

def classification(n):
    if n<51:
        return 1
    if n>51:
        return 2
    
input_data=readExcel()
# print(input_data)
data=[[x]for x in input_data]

result=[2,2,2,1,1,1]

textresult=[devision(x) for x in result]

print ("result numeric",result)
print ("result text",textresult)
print ("input data",input_data)

classifire=tree.DecisionTreeClassifier()
model = classifire.fit(data,result)


plt.plot(data,result,color='red')
plt.scatter(data,result,color='blue',marker='o')
plt.grid()
plt.xlabel('data')
plt.ylabel('devision')
plt.title('data-devision')
plt.legend(["Actual Devision","Actual Devision"])
plt.show()
