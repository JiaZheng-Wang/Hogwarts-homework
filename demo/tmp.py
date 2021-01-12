# def warpper(func)


def func():
    while True:
        x = yield
        print("x:", x)
        if x == 11:
            break



f=func()
next(f)
f.send(1)
f.send(2)
f.send(3)
