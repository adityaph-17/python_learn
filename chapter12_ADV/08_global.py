# Without global
a = 10 #global variable

def fun1():
    a = 20 # local variable only inside func
    print(a)

def fun2():
    global a
    a = 30
    print(a)

fun1() #output = 20
# now a = 10 but after fun2() a = 30
fun2()

