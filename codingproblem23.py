
"""Run length Encoding
ex-AABCDEEA is written as A2B1C1D1E2A1"""
s=input("Enter a string having alphabets only: ")
s=s.upper()
#list is created that contains each string elements
l1=list(s)
s1=" "
count=1
for i in range(0,len(l1)-1):
    if l1[i]==l1[i+1]:
        #To count occurence of each alphabets
        count=count+1
    else:
        s1=s1+l1[i]+str(count)
        count=1
s1=s1+l1[i+1]+str(count)
print(s1)


