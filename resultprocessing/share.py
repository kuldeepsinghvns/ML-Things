from sklearn import tree
import matplotlib.pyplot as plt

def devision(n):
    if n==2:
        return "false"
    return "true"
def classification(n):

    if n<51:
        return 2
    return 1

# def devision(n):
#     if n==2:
#         return "2nd"
#     return "1st"

def classification(n):
    if n<51:
        return 1
    if n>51:
        return 2
    
inputdata = [28,50,42,60,51,75]
inputdata.sort()

data=[[x]for x in inputdata]

result=[2,2,2,1,1,1]

textresult=[devision(x) for x in result]

print ("result numeric",result)
print ("result text",textresult)
print ("input data",inputdata)

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



