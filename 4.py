"""
You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8
Sample Output :
31
"""

a=[1,2,3,4,5,6,7,8,9,10,11,12]
b=31
c=28
d=31
e=30
f=31
g=30
h=31
i=30
j=31
k=30
l=31
m=30
x=int(input())
if x==1:
    print(b)
elif x == 2:
    print(c)
elif x == 3:
    print(d)
elif x == 4:
    print(e)
elif x == 5:
    print(f)
elif x == 6:
    print(g)
elif x == 7:
    print(h)
elif x == 8:
    print(i)
elif x == 9:
    print(j)
elif x == 10:
    print(k)
elif x == 11:
    print(l)
elif x == 12:
    print(m)
elif x ==0:
    print("Error")
elif x>12:
    print("Error")
