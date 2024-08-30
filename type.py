# int, float, str
# list, dist, set, tumple

a = 10
b = 11

# list
# multiple data Store
# eg
# a = [1,2,4]
# print (type(a))


# b = ["Ganesh", 1, 0, 1.2]
# print(b[0])
# print(b[-2])

# teachers = ["ram", "shyam", "hari", "gita", "sita", "rama", "priti"]
# print(teachers[1:3])
# print(teachers[2:])
# print(teachers[:4])
# print(teachers[:])

# print(len(teachers))

# test = [1, 2, 4, ["Ganesh", "Amgain"]]
# x = test[-1]
# print(x[-1])
# print(test[-1][0])
# print(test[3][1])
# print(test[:2])

# test.append("ramesh")
# print(test)
# print(test)
# test.append("subash")
# print(test)

# print("before append")
# a = []
# print(a)
# print("after append")
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# print(a)

# print("insert")
# test = [1,2,3,4,5]
# test.insert = [2,"ganesh"]
# print(test)
# test.insert = [2,"ram"]
# print(test)

# a = [1,2,3,4,5]
# b = ["ram", "shyam", "hari"]
# print(a+b)

# Class Exercise
# a = int(input("inter a number: "))
# if(a%2==0):
#     list = [a]
#     print("added to lit")
#     print(list)
# else:
#     print("not added to list")

# b = float(input('enter a number'))
# list = []
# if(b%2==0):
#     list.append(b)
# print(b)


# Extend
test = [1,2,3,4,5,6,7,8,9,10]
test2 = ["a", "b", "c"] 
test.extend(test2)
print(test)

# Delete
del test[-1]
print(test)

# Remove
aa = [1,1,1,1,1]
aa.remove(1)
print(aa)

# Pop
bb = [1,2,3,4,5]
bb.pop()
print(bb)


# Clear
xy = [1,2,3,4,5]
xy.clear()
print(xy)


# Count
p = aa.count(1)
print (p)
