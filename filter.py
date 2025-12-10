'''nums = [(1,11),(2,22),(3,33),(4,44),(5,55)]
even = list(filter(lambda ele : ele[1]%2==0 ,nums))

print(even)
'''





















'''
l1 = [(1,0,1,3),(2,0,1,2),(0,9,1,2),(3,-9,1,2)]
nested_nums = list(filter(lambda ele : sum(ele)<10,l1))
print(nested_nums)
'''























'''
d1 = {'One':1,'Zero':0,'Three':3,'Eight':8,'Nine':9}
digits = dict(filter(lambda ele:ele[0][0] in "AEIOUaeiou",list(d1.items())))
print(digits)
print(list(d1.items()))
'''



















'''
words = ['5M5','WI-5','3sha','9tara','1aja','1:37PM']
sum_dig = list(filter(lambda char : sum(tuple(filter(lambda x : 0<=int(x)<=9,char))),words))
print(sum_dig)
'''
