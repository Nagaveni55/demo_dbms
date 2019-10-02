##with open(lab1.csv) as f:
  #  reader = csv.reader(f, delimiter="\t")
   # for i in reader:
    #    print(i[0])

import os
import csv

pathName = os.getcwd()

numFiles = []
fileNames = os.listdir(pathName)
for fileNames in fileNames:
    if fileNames.endswith(".csv"):
        numFiles.append("actual.csv")

for i in numFiles:
    file = open(os.path.join(pathName, i), "rU")
    reader = csv.reader(file, delimiter=',')
    for column in reader:
        b=column[0][0]
        print(b)
        
        
import pandas as pd

import math
def calculate(a):
	

	y1=math.floor(a)
	y2=math.ceil(a)
	data = pd.read_csv("lab1.csv", index_col ="windspeed")

	x1 = data.loc[y1] 
	x2 = data.loc[y2]
	print(y1)
	print(y2)
	r=x1[0]
	q=x2[0]
	print(q)
	print(r)
	if (y1==y2 or q==r):
		return q
	else:
		m=(y2-y1)/(q-r)
		print(m)
		ans=((a-y1)/m)+r
		return ans
		#print(ans)
calculate(4.5)