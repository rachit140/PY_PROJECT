data = input()
u=l=d=a=0
for i in range (len(data)):
    if (data[i].isupper()):
        u =u+1
    if (data [i].islower()):
        l = l+1
    if (data[i].isalpha()):
        a=a+1
    if (data[i].isdigit()):
        d=d+1
print ("number of uppercase letter ",u)  
print ("number of lowercase letter ",l)
print ("number of alphabets letter ",a)
print ("number of digits letters ",d)





