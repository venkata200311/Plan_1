'''
largest_num = lambda l1,k : sorted(set(l1))[-k] 

print(largest_num([5,1,9,5,7,9],2))
'''











'''
from functools import reduce
k = lambda l1 : list(reduce(lambda n1,n2 : n1+n2 ,l1))

print(k([[1,2],[3,4],[5]]))
'''













# l1 = [(1,3),(2,3),(4,5)]


# # k = lambda l1 : sorted(l1,key=lambda x : x[1],reverse=True)
# s = sorted([(1,3),(2,3),(4,5)],key=lambda x : l1[l1.index(x,0,len(l1))] if(l1.index(x,0,len(l1))+1==len(l1) and l1[l1.index(x,0,len(l1))]>l1[l1.index(x,0,len(l1))+1]) else l1[l1.index(x,0,len(l1))+1])

# print(s)

# # k = lambda l1 : reduce(lambda f,n : f if(f[1]>n[1]) else ((f if(f[0]>n[0]) else n) if(f[1]==n[1]) else n),l1)
# # res = [k(l[i:])  for i in range(len(l)) ]

# # print(res)
# # print(k([(1,3),(2,3),(4,5)]))


# res = filter()
















'''
k = lambda l1 : sorted(l1,key=lambda x : (-x[1],x[0]))

print(k([(2,3),(1,3),(4,2),(1,5)]))
'''












'''
k = lambda s1 : "".join([i.lower() for i in s1 if(i.isalnum())])==("".join([i.lower() for i in s1 if(i.isalnum())]))[::-1]

print(k("Race car"))
'''








'''
s1 = "venkata"
l1 = ["v","e","n","k","a","t","a"]
print("".join(s1))
print("".join(l1))
'''









# k = lambda s1 : {'vowels': i for i in range(0,len(s1)) if(s1[i] in "AEIOUaeiou")}

# print(k("venkata"))























'''
marks = [90,85,70,35,40,55,63]

def mark(m):
    for i in range(0,len(m)):
        if(type(m[i])==int):
            if(m[i]>85 and m[i]<=100):
                m[i] = "A"
            elif (m[i]>65 and m[i]<=85):
                m[i] = "B"
            elif (m[i]>45 and m[i]<=65):
                m[i] = "C"
            elif(m[i]>=35 and m[i]>0):
                m[i] = "D"
    return m

k = lambda m1 : list(filter(lambda ele : ele,mark(m1)))

print(k(marks))
'''









s= [("Ravi",45),("Anita",78),("Kiran",90),("Meena",32),("Arjun",55),("Lakshmi",88)]

k = lambda l1 : dict(list(filter(lambda ele : ele[1]>35,l1)))

# print(k(s))


k1 = lambda l2 : {i[0].upper():i[1] for i in l2}

print(k1(s))
