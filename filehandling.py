# f = open("homework.py", "r")
# a = str(f.read())

# g = open ("amgain.py", "w")
# g.write(a)

# f = open("ganesh.py", "r")
# g = open("amgain.py", "a")
# g.write(f.read())


# try:
#     a = open("cloth.py", "x")
# except:
#     print('file already excits')

f = open("ganesh.py", "w+")
f.write("trying")
print(f.read())