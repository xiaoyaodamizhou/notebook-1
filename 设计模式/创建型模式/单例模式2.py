class singleton:
    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError("singletons must be accessed through instance()")

    def __instancecheck__(self, instance):
        return isinstance(instance, self._decorated)


@singleton
class A:
    def __init__(self):
        pass

    def display(self):
        return id(self)


if __name__ == '__main__':
    s1 = A.Instance()
    s2 = A.Instance()
    print(s1 is s2)
    print(s1.display())

