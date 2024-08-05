import csv
import sys
from collections import Counter
from pandas import *
 
# reading CSV file
def Validation(file_path):
    data = read_csv(file_path)
    csv_file = csv.reader(open(file_path), delimiter=",")
    # converting column data to list
    month = data['Path'].tolist()
    fc = data['Path'].tolist()
    fw = data['Status'].tolist()
    fv = data['Valid Date From'].tolist()
    a=[]
    b=[]
    listt=[]
    # printing list data
    l=len(fc)
    for i in range(l):
        if "dmerge.exe" in fc[i] or "spice3.exe" in fc[i]:
            continue
        else:
            a.append(fc[i]+fw[i])

    le=len(a)
    for i in range(le):
        if (("Valid" not in a[i]) or ("InValid" in a[i])):
            b.append(fc[i]+"-->"+fw[i])
    cleanedList = [x for x in fv if str(x) != 'nan']
    counter = Counter(fv)
    datediff=min(counter, key=counter.get)
    try:
        if len(b)and len(datediff):
            print("Invalid Exes as below:-")
            print("-----------------------")
            print(*b,sep="\n")
            print("-----------------------")
            for row in csv_file:
                if datediff == row[4]:
                     listt.append(row[0]+"-->"+row[4])
            print("error in valid date form")
            print("------------------------")
            print("The result is RED")
            print(*listt,sep="\n")
        elif len(datediff):
            for row in csv_file:
                if datediff == row[4]:
                     listt.append(row[0]+"-->"+row[4])
            print("error in valid date form")
            print("------------------------")
            print(*listt,sep="\n")
            print("The result is RED")
        else:
            print("EXEs are having valid digital certificates -- The result is GREEN")
    except:
        if len(b) :
            print("Invalid Exes as below:-")
            print("-----------------------")
            print(*b,sep="\n")
            print("-----------------------")
            print("The result is RED")
        else:
            print("EXEs are having valid digital certificates -- The result is GREEN")

file_path = r'C:\apps\Digital_testing_capital_2207.csv'
Validation(file_path)
file_path = r'C:\apps\Digital_testing_capital_21.csv'
Validation(file_path)
file_path = r'C:\apps\Digital_testing_capital_20.csv'
Validation(file_path)
