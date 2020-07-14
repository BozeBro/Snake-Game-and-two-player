import functools


class Ex:
    def wrapper(func):
        @functools.wraps(func)
        def wrap(self):
            print("inside wrap")
            return func(self)

        return wrap

    @wrapper
    def method(self):
        print("method")


m = Ex()
m.method()
