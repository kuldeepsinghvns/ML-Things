import matplotlib.pyplot as plt
import numpy as np 
from resultprocessing.student import student
from resultprocessing.subject import Subject
from resultprocessing.menu import menu
result = {}
while True:
    print("0-Exit,1-Add,2-Search,3-plot")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        st = student()
        physics = Subject()
        chemistry = Subject()
        result[st.rollno] = [st, physics, chemistry]
        print("Added")
        continue
    if option == 2:
        rollno = int(input("Roll No= "))
        data = result.get(rollno)
        if data is None:
            print("Not found")
            continue
        print("Student ", data[0])
        print("Subject 1 ", data[1])
        print("Subject 2 ", data[2])
    if option ==3:
        x=list(range(101))
        y=[x*x for x in x]
        plt.scatter(x,y, color="pink")
        plt.plot(y,x)
        plt.show()
        continue
        

