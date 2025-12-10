'''
is_Palindrome = lambda num : int(str(num)[::-1])==num

print(is_Palindrome(12321))
'''
























'''
Palindromes_words = lambda l1 : [word for word in l1 if (word[::-1]==word)]

pal_words = Palindromes_words(['SYS','PIPE','SMS','SIR','KICK','TAB'])
print(pal_words)
'''

























'''
Perfect_number = lambda num : sum(tuple(i for i in range(1,num) if(num%i==0)))==num

print(Perfect_number(28))
'''