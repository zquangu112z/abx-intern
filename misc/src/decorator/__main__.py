from time import time
import functools


def logTimer(my_function):
    def wrap():
        start = time()
        my_function()
        end = time()
        print("Func costs %fus" % ((end - start) * 1000))

    return wrap


def logTimer2(my_function):
    @functools.wraps(my_function)
    def wrap():
        start = time()
        my_function()
        end = time()
        print("Func costs %fus" % ((end - start) * 1000))

    return wrap


def func1():
    print("func1!")


@logTimer
def func2():
    print("func2!")


@logTimer2
def func3():
    print("func2!")


if __name__ == '__main__':
    print("Name of func1 %s" % func1.__name__)
    func1 = logTimer(func1)
    func1()
    print("Name of func1 %s" % func1.__name__)

    func2()
    print("Name of func2 %s" % func2.__name__)

    func3()
    print("Name of func3 %s" % func3.__name__)
