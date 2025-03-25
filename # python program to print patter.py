# python program to print patter
# by rachit sharma on 01.05.2023

n=int(input("enter the number of rows:"))
for row in range (1,n+1):
    for col in range (1,row+1):
        print(row,end="")
    print()
