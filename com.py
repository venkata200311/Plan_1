'''
lst = [[1,2],[3,4,5],[6]]
lst = [j for sub in lst for j in sub]


print(lst)
'''










'''
words = ["level","hello","radar","world","madam"]

lst = [wor for wor in words if(wor==wor[::-1])]
print(lst)
'''










'''
nums = [1,2,3,4,5,6]

lst = [i**2 if(i%2==0) else i**3 for i in nums]

print(lst)
'''
















'''
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

lst = [[l[j] for l in mat] for j in range(len(mat[0]))]

print(lst)
'''


               











 
'''
a = [1,2,3]
b= [4,5]

lst = [(i,j) for i in a for j in b]

print(lst)
'''










'''
d = {"a":1,"b":2,"c":3}

d1 = {i[1]:i[0] for i in d.items()}

print(d1)
'''















'''s = "banana"

d = {"count":i for i in range(len(s)+1)}

print(d)
'''













'''
scores = {"ram":83,"shyam":40,"geeta":92,"ravi":55}

d1 = {i[0]:i[1] for i in scores.items() if(i[1]>60)}

print(d1)
'''











'''
nums = [1,-1,2,-2,3,-3]

s = {i**2 for i in nums}

print(s)'''














'''
s1 = "programming"
s2 = "algorithm"

s = {i for i in s1 for j in s2 if(i==j)}

print(s)
'''















'''
lst1 = [[j[i] for j in mat] for i in range(len(mat[0]))]
print(lst1)
'''