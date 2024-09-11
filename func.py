# def test():
#     print("this is test")

# test()

# def add():
#     a = 2+2
#     data =[]
#     for i in range(1,5):
#         data.append(i)

#     return data

# print(add())

# def myinfo():
#     print(f"my name is ganesh")
# myinfo()

# def myinfo(name,addres):
#     print(f"my name is {name}.I live in {addres} ")
# myinfo("ganesh",'palungtar')

# def kantipur(title, content, author):
#     print("holiday", "teej", "ganesh")
# kantipur("title", "content", "author")

def test(a,b,c):
    print("hello")

test(1,2,3)

def keyword_arg(surname, name):
    print(name, surname)

keyword_arg(name="ganesh", surname="amgain")

def test2(*args):
    total = 0
    for i in args:
        total=total+i
    return total

a = test2(1,2,3,4,1212) 
print(a)

def test3(**data):
    print("hello")
    print(data)
    print(type(data))

test3(name="suman", surname="sharma", age=32)


def hello(*args, **kwargs):
    print("positional", args)
    print("keyword", kwargs)
    return args, kwargs
print(hello(1,2,3,4,name="hello"))



