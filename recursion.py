def fact(n):
    if n==1 or n==0:
        return 1
    return n * fact(n-1)

print(fact(5))

# a = [1,2[4,1,[1,[1,[1,4]]]]]
# a = isinstance(a, str)
# print(a)

# add 1 to 10 ny Using Recursion
def sum (n):
    if n == 1:
        return 1
    else:
        return n + sum (n - 1)

# Calculate the sum from 1 to 10
result = sum (10)
print(result)  
# Output will be 55


