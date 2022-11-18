import numpy as np
import math
from collections import Counter
documents1=[]
ids=[]
queries=[]
output = ""
def getQueries():
    queries = []
    with open('queries.txt') as qF:
        for e in qF:
            queries.append(e.strip().split())
        return queries 
def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta
dict1 = {}
with open('docs.txt') as dF:
    key = 1
    for line in dF:
        dict1[key] = list(line.strip().split())  
        key+=1    
print()

num = 0 
with open("docs.txt","r") as file1:
    for line in file1:
        temp = []
        for word in line.split():
            temp.append(word)
            if word not in documents1:
                documents1.append(word)
                num+=1
        ids.append(temp)

print()

with open("queries.txt","r") as file2:
    for line in file2:
        line = line.strip("\n")
        queries.append(line)
print()
output += "Words in dictionary: "+str(len(documents1)) +"\n"
documents1.sort()
queryVector = []

for i in range(len(queries)):
    positions = ""
    length = len(queries[i].split())
    queryVector = [1 for lk in range(len(list(queries[i].split())))]
    output += "Query: "+queries[i] +"\n" 
    for j in range(len(ids)):
        num1 = 0
        for k in queries[i].split():
            if k in ids[j]:
                num1+=1
        if num1==length:
            positions  = positions + str(j+1) + " "
    
    output += "Relevant documents: "+"".join(map(str,positions)) +"\n" 
    dict2 = {}
    positions = [ int(x) for x in positions.strip().split() ]
    for k1, v1 in dict1.items():
        if k1 in positions:
            dict2[k1] = v1
    
    documentVector = [0 for i in range(len(documents1))]     #generate cocument vector with 0
    queryVector1 = [0 for i in range(len(documents1))]       #generate query vector with 0
    
    queryVector2 = queries[i].split()  
    dict3 = {}
    for k5, v5 in dict2.items():
        tempList = []
        tempList2 = []
        for snglE in range(len(documents1)):
            temp = documentVector[snglE] = v5.count(documents1[snglE])
            temp2 = queryVector1[snglE] = queryVector2.count(documents1[snglE])
            tempList.append(temp)
            tempList2.append(temp2)
       
        dict3[k5] = tempList
    dict4 = {}
    for k2, v2 in dict3.items():
        dict4[k2] = calc_angle(queryVector1, v2) 
  
    dict3_view = [(v3, k3) for k3, v3 in dict4.items() ]
    dict3_view.sort()
    for k4, v4 in dict3_view:
        output += "%s  %.4f" % (v4,k4) +"\n" 

file = open("Output.txt", "w")
file.write(output) 
file.close()