import time
import pandas as pd
from selenium import webdriver

def grade (Division):
    if Division >=60:
        return '1st Division'
    if Division >=50:
        return '2nd Division'
    if Division >=40:
        return '3rd Division'
    else:
        return 'Fail'


def readExcel():

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df = pd.read_csv('studentdata.csv')
    rollnum = df['rollnum']
    name = df['name']
    hindi = df['hindi']
    english = df['english']
    math = df['math']
    # print(df)
    # return rollnum, name, hindi, english, math

    df['Total Marks'] = hindi+english+math
    total=df["Total Marks"]
    df['Division']=(total/3)

    df['grade'] = df['Division'].apply(grade) 
    print(df)

    return rollnum,name,hindi,english,math

rollnum,name,hindi,english,math=readExcel()







