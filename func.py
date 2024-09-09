def test():
    print("this is test")

test()

def add():
    a = 2+2
    data =[]
    for i in range(1,5):
        data.append(i)

    return data

print(add())

def myinfo():
    print(f"my name is ganesh")
myinfo()

def myinfo(name,addres):
    print(f"my name is {name}.I live in {addres} ")
myinfo("ganesh",'palungtar')

def kantipur(title, content, author):
    print("holiday", "teej", "ganesh")
kantipur("title", "content", "author")