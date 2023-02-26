# Name:                     Task 5: Cubed Numbers
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             February 25, 2023
# Date Last Modified:       February 26, 2023

cubeDict = {}

for number in range(1,11):
   
    cubedNum = number * number * number
    cubeDict[number] = cubedNum
    
print(cubeDict)