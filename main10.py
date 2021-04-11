from bisect import bisect,insort
from random import randint,seed
li1=[]#let's generate 2 random lists
li2=[]
for i in range(10):
        li1.append(randint(1,100))
        li2.append(randint(1,100))

print(li1)
print(li2)

#now by using the bisect library let's merge li1 into li2 and sort both of them
#at the same time.
li1.sort()
li2.sort()
for element in li2:
        insort(li1,element)

print(li1)



                
                

