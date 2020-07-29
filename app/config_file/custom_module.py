import time

def func():
    print("called func")
    time.sleep(2)
    _internal_func()


def _internal_func():
    print("called _internal_func")
    time.sleep(3)


class ClassFunction:
    def another_function(self):
        print("called another_function")
        time.sleep(2)
        _internal_func()